import random

def main():
    print("Khansole Academy")

    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    expected = num1 + num2

    print(f"What is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))

    if user_answer == expected:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {expected}")

if __name__ == '__main__':
    main()
