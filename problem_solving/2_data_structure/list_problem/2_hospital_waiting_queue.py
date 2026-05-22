patient = ["Rin", "Sam", "Yuki"];
patient.append("Leo");

remove_patient = patient.pop(0);
print("Now calling:", remove_patient);
print("Remaining queue:", patient);
print("Patients waiting", len(patient));