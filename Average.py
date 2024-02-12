# average.py (on fast_forward_test branch)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [float(num) for num in user_input.split()]
    average = calculate_average(numbers)
    print(f"The average is: {average}")
