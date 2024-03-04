# average.py (on fast_forward_test branch)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_largest(numbers):
    return max(numbers)

def find_smallest(numbers):
    return min(numbers)

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [float(num) for num in user_input.split()]
    
    average = calculate_average(numbers)
    largest = find_largest(numbers)
    smallest = find_smallest(numbers)
    
    print(f"The average is: {average}")
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")
