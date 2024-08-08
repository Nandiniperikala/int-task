import sys
import json
import random

def perform_subtraction(numbers):
    result = [numbers[i] - numbers[i + 1] for i in range(len(numbers) - 1)]
    print("Subtraction results (comma-separated):", ", ".join(map(str, result)))

def perform_multiplication(numbers):
    multiplication_result = 1
    for number in numbers:
        multiplication_result *= number
    
    result_dict = {
        "inputNumber1": numbers[0],
        "inputNumber2": numbers[1],
        "inputNumber3": numbers[2],
        "inputNumber4": numbers[3],
        "inputNumber5": numbers[4],
        "inputNumber6": numbers[5],
        "Multiplication": multiplication_result
    }
    
    with open('result.json', 'w') as f:
        json.dump(result_dict, f, indent=4)
    
    print("Multiplication result stored in result.json")
    print(json.dumps(result_dict, indent=4))

def pick_random_number(numbers):
    print("Randomly picked number:", random.choice(numbers))

def print_sorted(numbers, reverse=False):
    sorted_numbers = sorted(numbers, reverse=reverse)
    order = "highest to lowest" if reverse else "lowest to highest"
    print(f"Numbers sorted ({order}):", sorted_numbers)

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Please provide exactly 6 numbers as command line arguments.")
        sys.exit(1)
    
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("All command line arguments must be integers.")
        sys.exit(1)

    while True:
        print("\nMenu:")
        print("1. Perform subtraction and show output on screen (comma separated).")
        print("2. Perform multiplication and store result in a JSON file.")
        print("3. Pick a random number and show it on screen.")
        print("4. Print sorted (highest to lowest) array/list numbers.")
        print("5. Print sorted (lowest to highest) array/list numbers.")
        print("6. Exit.")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            perform_subtraction(numbers)
        elif choice == '2':
            perform_multiplication(numbers)
        elif choice == '3':
            pick_random_number(numbers)
        elif choice == '4':
            print_sorted(numbers, reverse=True)
        elif choice == '5':
            print_sorted(numbers)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
