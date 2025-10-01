import random

def detect_stress(heart_rate, blood_pressure):
    if heart_rate > 100 or blood_pressure > 140:
        return "High Stress"
    elif heart_rate > 80 or blood_pressure > 120:
        return "Moderate Stress"
    else:
        return "Low Stress"

def provide_recommendations(stress_level):
    if stress_level == "High Stress":
        return random.choice([
            "Take a few deep breaths and focus on the present moment.",
            "Try progressive muscle relaxation to release tension.",
            "Listen to calming music or nature sounds.",
            "Take a short walk outside to clear your mind.",
            "Practice mindfulness meditation to reduce stress."
        ])
    elif stress_level == "Moderate Stress":
        return random.choice([
            "Take a short break and do some stretching exercises.",
            "Try journaling to express your emotions.",
            "Practice gratitude by thinking of three things you're thankful for.",
            "Engage in a hobby or activity that brings you joy.",
            "Take a power nap to recharge."
        ])
    else:
        return random.choice([
            "Keep up the good work! Continue to prioritize self-care.",
            "Try to maintain a healthy work-life balance.",
            "Practice self-compassion and be kind to yourself.",
            "Engage in activities that promote relaxation and calmness.",
            "Get enough sleep and maintain a consistent sleep schedule."
        ])

def session():
    name = input("Please enter your name: ")
    medical_problem = input("Do you have any medical problems we should be aware of? (yes/no): ")
    if medical_problem.lower() == "yes":
        medical_problem_details = input("Please describe your medical problem: ")
    else:
        medical_problem_details = "None"

    try:
        heart_rate = int(input(f"{name}, please enter your heart rate (beats per minute): "))
        blood_pressure = int(input(f"{name}, please enter your blood pressure (mmHg): "))
        stress_level = detect_stress(heart_rate, blood_pressure)
        print(f"\nBased on your heart rate ({heart_rate} bpm) and blood pressure ({blood_pressure} mmHg), your stress level is: {stress_level}\n")
        print("Recommendation:", provide_recommendations(stress_level))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def main():
    print("Welcome to the Stress Detection and Recommendation System!")
    while True:
        session()
        cont = input("\nWould you like to continue? (yes/no): ")
        if cont.lower() != "yes":
            print("Thank you for using the Stress Detection and Recommendation System!")
            break

if __name__ == "__main__":
    main()
