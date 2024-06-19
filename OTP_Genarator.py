import random

def generate_otp(length):
    """Generate a random numeric OTP of given length."""
    digits = "0123456789"
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

def main():
    print("Welcome to the OTP Generator!")
    print("Please specify the length of the OTP to generate.")

    # Input OTP length from user
    while True:
        try:
            length = int(input("Enter the length of the OTP: "))
            if length <= 0:
                print("Please enter a valid OTP length (greater than zero).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for OTP length.")

    # Generate the OTP
    otp = generate_otp(length)

    # Display the generated OTP
    print(f"Generated OTP: {otp}")

if __name__ == "__main__":
    main()
