
# Exercise 1

def multiply_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = multiply_or_sum(num1, num2)
print("Result:", result)

# Exercise 2

def print_sum_of_current_and_previous(n):
    previous_number = 0
    for i in range(1, n + 1):
        current_number = i
        total_sum = previous_number + current_number
        print("Current number:", current_number, "Previous number:", previous_number, "Sum:", total_sum)
        previous_number = current_number

# Iterate through the first 10 numbers
print_sum_of_current_and_previous(10)

# Exercise 3

def print_characters_at_even_index(input_string):
    for index in range(len(input_string)):
        if index % 2 == 0:
            print(input_string[index])

# Accepting input from the user
user_input = input("Enter a string: ")
print("Characters present at even index numbers:")
print_characters_at_even_index(user_input)

# Exercise 4

def remove_chars(input_string, n):
    if n < len(input_string):
        return input_string[n:]
    else:
        return "n must be less than the length of the string."

# Example usage:
print(remove_chars("pynative", 4))  # Output: tive
print(remove_chars("pynative", 2))  # Output: native

# Exercise 5

def check_first_and_last_same(numbers):
    if numbers[0] == numbers[-1]:
        print("First and Last Numbers are same")
    else:
        print("Not Same")

# Example usage:
numbers_list_1 = [1, 2, 3, 4, 5, 1]
check_first_and_last_same(numbers_list_1)  # Output: First and Last Numbers are same

numbers_list_2 = [1, 2, 3, 4, 5, 6]
check_first_and_last_same(numbers_list_2)  # Output: Not Same

# Exercise 6

def print_divisible_by_5(numbers):
    for number in numbers:
        if number % 5 == 0:
            print(number)

# Example usage:
numbers_list = [10, 15, 20, 25, 30, 35]
print("Numbers divisible by 5:")
print_divisible_by_5(numbers_list)

# Exercise 7

def print_pattern(rows):
    for i in range(1, rows + 1):
        print((str(i) + ' ') * i)

# Example usage:
print_pattern(5)
 
# Exercise 8

def is_palindrome(number):
    # Convert the number to a string to make it iterable
    number_str = str(number)
    # Check if the number is equal to its reverse
    return number_str == number_str[::-1]

# Example usage:
num = 545
if is_palindrome(num):
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")

# Exercise 9

def create_new_list(list1, list2):
    new_list = []
    # Add odd numbers from the first list
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
    # Add even numbers from the second list
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result_list = create_new_list(list1, list2)
print("New list:", result_list)

# Exercise 10

def extract_digits_reverse(num):
    # Convert the number to a string and reverse it
    num_str = str(num)[::-1]
    # Print each digit separated by a space
    print(" ".join(num_str))

# Example usage:
num = 7536
extract_digits_reverse(num)
