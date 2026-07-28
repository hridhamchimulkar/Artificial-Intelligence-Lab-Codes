def ask(symptom):
    return input(f"Do you have {symptom}? ").upper() == "Y"


def diagnose():
    print("\nHello, I'm your AI Doctor")
    print("Please answer questions with Y/N")
    
    disease = None
    
    if ask("fever"):
        if ask("cough"):
            if ask("loss of taste") and ask("breathing difficulty"):
                disease = "COVID 19"
            elif ask("sneezing") or ask("runny nose"):
                disease = "Common Cold"
            elif ask("bodyache") or ask("headache"):
                disease = "Flu"
            else:
                disease = "Flu"
        
        else:
            if ask("chills") and ask("sweating"):
                disease = "Malaria"
            elif ask("weakness") and ask("stomach ache"):
                disease = "Typhoid"
            else:
                disease = "Flu"

    elif ask("cough"):
        if ask("bodyache") or ask("headache"):
            disease = "Flu"
        elif ask("sneezing") or ask("runny nose"):
            disease = "Common Cold"
        elif ask("loss of taste") and ask("breathing difficulty"):
            disease = "COVID 19"
        else:
            disease = "Common Cold"
            
    elif ask("stomach ache"):
        if ask("vomiting") or ask("diarrhoea"):
            disease = "Food Poisoning"
        elif ask("weakness") and ask("headache"):
            disease = "Typhoid"
        
    return disease


while True:
    print("\n----- Rule-Based Expert System -----")
    print("1. Start Diagnosis")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        disease = diagnose()
        if disease is None:
            print("\nNo strong disease detected")
        else:
            print(f"\nYou likely have {disease}")
    elif choice == 2:
        print("\nExiting...")
        break
    else:
        print("\nEnter a valid choice")            