from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days_to_add):
    """
    Calculate and display a future date by adding specified days to current date.
    
    Args:
        days_to_add (int): Number of days to add to the current date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    """
    Main function to demonstrate datetime operations.
    """
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()