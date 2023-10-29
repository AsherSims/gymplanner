# Import the random module to generate random selections from workout plans.
import random

# Define a dictionary "workout_plans" with predefined workout plans for different goals, levels, and specialisations.
workout_plans = {
    "beginner_bulk": ["Push-ups", "Squats", "Dumbbell Rows", "Planks"],
    "beginner_cut": ["Jumping Jacks", "Lunges", "Bicep Curls", "Crunches"],
    "beginner_maintain": ["Squats", "Dumbbell Rows", "Planks"],
    "intermediate_bulk": ["Bench Press", "Deadlifts", "Pull-ups", "Russian Twists"],
    "intermediate_cut": ["Box Jumps", "Leg Press", "Tricep Dips", "Hanging Leg Raises"],
    "intermediate_maintain": ["Jumping Jacks", "Lunges", "Bicep Curls"],
    "expert_bulk": ["Barbell Squats", "Overhead Press", "Chin-ups", "Chest Press"],
    "expert_cut": ["Clean and Jerk", " Deadlift", "Inverted Rows", "dips"],
    "expert_maintain": ["Deadlifts", "Squats", "Shoulder press"],
    "professional_bulk": ["Power Cleans", "Front Squats", "Muscle-ups", "Rows"],
    "professional_cut": ["sprints", "Hack Squats", "Push-ups", "Knee ups"],
    "professional_maintain": ["Bench Press", "Deadlifts", "Pull-ups", "Russian Twists"],
}

# Prompt the user to input their fitness goal, specialisation, and experience level.
goal = input("Enter your goal (Bulk, Cut, Maintain): ").lower()
specialisation = input("Specialization for this week (Upper, Lower, Whole Body): ").lower()
level = input("Enter your experience level (Beginner, Intermediate, Expert, Professional): ").lower()

# Check if the user's inputs are valid. If not, display an error message.
if goal not in ["bulk", "cut", "maintain"] or specialisation not in ["upper", "lower", "whole body"] or level not in ["beginner", "intermediate", "expert", "professional"]:
    print("Incorrect input. Please enter one of the options.")
else:
    # Construct a key based on the user's experience level and fitness goal.
    key = f"{level}_{goal}"
    # Check if the  key is in the workout plans dictionary.
    if key not in workout_plans:
        print("Sorry, no workout plan available for this combination of level and goal.")
    else:
        # Display the user's selected fitness goal, specialisation, and experience level.
        print("\nYour Weekly Workout Plan:")
        print(f"Goal: {goal.capitalize()}")
        print(f"Specialization: {specialisation.capitalize()}")
        print(f"Experience Level: {level.capitalize()}\n")
        print("Workout Plan for the Week:")
        # Generate a weekly workout plan for five days based on specialisation and random exercise selection.
        for day in ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]:
            if specialisation == "upper":
                selected_exercises = random.sample(workout_plans[key], 2)
                print(f"{day}: {', '.join(selected_exercises)}")
            elif specialisation == "lower":
                selected_exercises = random.sample(workout_plans[key], 1)
                print(f"{day}: {', '.join(selected_exercises)}")
            elif specialisation == "whole body":
                selected_exercises = random.sample(workout_plans[key], 3)
                print(f"{day}: {', '.join(selected_exercises)}")
            else:
                print(f"{day}: Rest")
