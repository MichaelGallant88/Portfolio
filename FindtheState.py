# Exploring Arrays/Lists: Find the State
# This program displays a list of states and allows the user to
# enter a number between 0 and 7 to select a state from the list.
# It includes error handling for invalid or non-numeric input.

# List of exactly eight states
states = [
    "Vermont",
    "Massachusetts",
    "New Hampshire",
    "Texas",
    "Florida",
    "California",
    "Maine",
    "New York"
]

# Show the list to the user
print("Here is the list of states:")
for index, state in enumerate(states):
    print(f"{index}: {state}")

# Loop until valid input is entered
while True:
    user_input = input("\nEnter a number between 0 and 7 to select a state: ")

    # Check if input is numeric
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    # Convert to integer
    choice = int(user_input)

    # Check if number is within range
    if 0 <= choice <= 7:
        print(f"The state at position {choice} is {states[choice]}.")
        break
    else:
        print("Invalid number. Please enter a number between 0 and 7.")
