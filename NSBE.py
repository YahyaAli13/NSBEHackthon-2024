import heapq
from pymongo import MongoClient

# Replace 'your_password' with your actual password
connection_string = 'mongodb+srv://Yahya:Yahya-13@cluster0.8gzoanx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# MongoDB connection setup
try:
    client = MongoClient(connection_string)
    db = client['hospital_database']  # Use your database name
    patients_collection = db['patients']  # Use your collection name
    print("Connected to MongoDB.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

class Patient:
    def __init__(self, id, name, symptoms, vitals):
        self.id = id
        self.name = name
        self.symptoms = symptoms  # List of symptoms
        self.vitals = vitals  # Dictionary for vitals, e.g., {'heart_rate': value}
        self.severity_score = 0

class TriageSystem:
    def __init__(self):
        self.waiting_list = []  # This will act as our priority queue

    def calculate_severity_score(self, patient):
        # Example scoring system
        score = 0
        if 'high blood pressure' in patient.symptoms:
            score += 5
        if 'Fever' in patient.symptoms:
            score += 2
        if 'Cough' in patient.symptoms:
            score += 1
        if 'Chest Pain' in patient.symptoms:
            score += 3        
        if 'Bleeding' in patient.symptoms:
            score += 4  
        if 'Hard breathing' in patient.symptoms:
            score += 5  
        if 'Light head' in patient.symptoms or 'dizzy' in patient.symptoms:
            score += 2  
        if patient.vitals.get('heart_rate', 0) > 100:
            score += 3  # Adding to the score if heart rate is over 100
        patient.severity_score = score

    def save_patient_to_db(self, patient):
        try:
            # Convert patient object to dictionary for MongoDB
            patient_dict = {
                'id': patient.id,
                'name': patient.name,
                'symptoms': patient.symptoms,
                'vitals': patient.vitals,
                'severity_score': patient.severity_score
            }
            # Insert patient data into MongoDB
            patients_collection.insert_one(patient_dict)
            print(f"Patient {patient.name}'s data saved to MongoDB.")
        except Exception as e:
            print(f"An error occurred while saving to MongoDB: {e}")

    def add_patient(self, patient):
        self.calculate_severity_score(patient)
        # Use negative severity score because heapq is a min-heap
        heapq.heappush(self.waiting_list, (-patient.severity_score, patient.id, patient))
        # Save patient to MongoDB
        self.save_patient_to_db(patient)

    def add_patient_via_input(self):
        id = len(self.waiting_list) + 1  # Simple way to generate a unique ID
        name = input("Enter patient's name: ")
        symptoms_input = input("Enter patient's symptoms, separated by commas (e.g., fever, cough): ")
        symptoms = symptoms_input.split(', ')
        heart_rate = int(input("Enter patient's heart rate: "))
        vitals = {'heart_rate': heart_rate}

        new_patient = Patient(id=id, name=name, symptoms=symptoms, vitals=vitals)
        self.add_patient(new_patient)
        print(f"Added {name} with severity score {new_patient.severity_score} to the waiting list.")

triage_system = TriageSystem()
triage_system.add_patient_via_input()

# Optionally, you can process patients based on priority
# next_patient = triage_system.next_patient()
# if next_patient:
#     print(f"Next patient to see based on severity: {next_patient.name}")
# else:
#     print("No patients in the waiting list.")
