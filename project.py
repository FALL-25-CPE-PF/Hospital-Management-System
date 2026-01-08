# ==============================
# Hospital Management System
# Admin View + Patient View
# Core Python Only (No Libraries)
# ==============================

patients = {}

# ---------- FILE HANDLING ----------

def load_data():
    try:
        file = open("hospital_data.txt", "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("|")

            # SAFETY CHECK (PERMANENT FIX)
            if len(parts) != 8:
                continue

            pid = parts[0]
            name = parts[1]
            age = parts[2]
            gender = parts[3]
            disease = parts[4]
            doctor = parts[5]

            history = []
            if parts[6] != "":
                history = parts[6].split(",")

            bill = []
            if parts[7] != "":
                for b in parts[7].split(","):
                    bill.append(int(b))

            patients[pid] = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctor,
                "history": history,
                "bill": bill
            }
        file.close()
    except FileNotFoundError:
        pass


def save_data():
    try:
        file = open("hospital_data.txt", "w")
        for pid, data in patients.items():
            history = ",".join(data["history"])

            bill_str = ""
            for b in data["bill"]:
                bill_str += str(b) + ","
            bill_str = bill_str[:-1]

            line = (
                pid + "|" +
                data["name"] + "|" +
                data["age"] + "|" +
                data["gender"] + "|" +
                data["disease"] + "|" +
                data["doctor"] + "|" +
                history + "|" +
                bill_str + "\n"
            )
            file.write(line)

        file.close()
    except:
        print("Error saving data!")
        
# ---------- ADMIN FUNCTIONS ----------

def add_patient():
    pid = input("Enter Patient ID: ")

    if pid in patients:
        print("Patient already exists!")
        return

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Age must be a number.")
        return

    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    doctor = input("Assign Doctor: ")

    # 🔹 NEW: INITIAL BILL AT REGISTRATION
    try:
        initial_bill = int(input("Enter Initial Bill Amount: "))
    except ValueError:
        print("Invalid bill amount. Patient not added.")
        return

    patients[pid] = {
        "name": name,
        "age": str(age),
        "gender": gender,
        "disease": disease,
        "doctor": doctor,
        "history": [],
        "bill": [initial_bill]   # bill added here
    }

    print("Patient added successfully with initial bill!") 
       
def view_patients():
    if not patients:
        print("No patients found.")
        return 
    for pid, data in patients.items():
        print("\nPatient ID:", pid)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Gender:", data["gender"])
        print("Disease:", data["disease"])
        print("Doctor:", data["doctor"])

        print("Medical History:")
        if not data["history"]:
            print("No history available.")
        for h in data["history"]:
            print("-", h)

        total = 0
        for b in data["bill"]:
            total += b
        print("Total Bill:", total)       
def assign_doctor():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return
    doctor = input("Enter New Doctor Name: ")
    patients[pid]["doctor"] = doctor
    print("Doctor updated successfully!")

def add_history():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return
    note = input("Enter medical note: ")
    patients[pid]["history"].append(note)
    print("Medical history added.")
def add_bill():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return
    try:
        amount = int(input("Enter bill amount: "))
        patients[pid]["bill"].append(amount)
        print("Bill added successfully.")
    except ValueError:
        print("Invalid amount!")  
def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("Total Patients:", len(patients))
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Assign / Change Doctor")
        print("4. Add Medical History")
        print("5. Add Bill")
        print("6. Back")
        
        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            assign_doctor()
        elif choice == "4":
            add_history()
        elif choice == "5":
            add_bill()
        elif choice == "6":
            save_data()
            break
        else:
            print("Invalid choice!")
            # ---------- PATIENT VIEW ----------
def patient_view():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return

    data = patients[pid]

    print("\n--- PATIENT DETAILS ---")
    print("Name:", data["name"])
    print("Age:", data["age"])
    print("Gender:", data["gender"])
    print("Disease:", data["disease"])
    print("Doctor:", data["doctor"])

    
