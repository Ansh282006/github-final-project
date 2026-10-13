def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    Formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100


def main():
    print("Simple Interest Calculator")
    print("--------------------------")

    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time (years): "))

        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest

        print(f"\nSimple Interest = {interest:.2f}")
        print(f"Total Amount     = {total_amount:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()