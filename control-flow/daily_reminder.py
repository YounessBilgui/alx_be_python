# daily_reminder.py
# Daily Task Reminder using conditional statements, Match Case, and loops

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    # Customize message based on priority for non-time-bound tasks
    match priority:
        case "high":
            reminder += ". Consider completing it soon."
        case "medium":
            reminder += ". Consider completing it when you have some time."
        case "low":
            reminder += ". Consider completing it when you have free time."
        case _:
            reminder += ". Consider completing it when convenient."
    
    print(f"Note: {reminder}")
