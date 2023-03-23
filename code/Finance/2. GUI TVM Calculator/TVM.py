import math

def calculate_FV(PV, IY, N, compound_frequency=1):
    return PV * math.pow((1 + (IY / (compound_frequency * 100))), compound_frequency * N)

def calculate_PV(FV, IY, N, compound_frequency=1):
    return FV / math.pow((1 + (IY / (compound_frequency * 100))), compound_frequency * N)

def calculate_PMT(PV, IY, N):
    r = IY / 100
    return PV * r / (1 - math.pow(1 + r, -N))

def calculate_N(PV, IY, PMT):
    r = IY / 100
    return -math.log(1 - (PV * r / PMT)) / math.log(1 + r)

def calculate_IY(PV, FV, N):
    return ((FV / PV) ** (1 / N) - 1) * 100

def main():
    print("TVM Calculator")
    print("1. Calculate Future Value (FV)")
    print("2. Calculate Present Value (PV)")
    print("3. Calculate Payment (PMT)")
    print("4. Calculate Number of Years (N)")
    print("5. Calculate Interest Rate (IY)")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        PV = float(input("Enter the Present Value (PV): "))
        IY = float(input("Enter the annual interest rate (IY) as a percentage: "))
        N = float(input("Enter the number of years (N): "))
        compound_frequency = int(input("Enter the number of times interest is compounded per year: "))

        FV = calculate_FV(PV, IY, N, compound_frequency)
        print(f"The future value (FV) of your investment is: ${FV:.2f}")

    elif choice == 2:
        FV = float(input("Enter the future value (FV): "))
        IY = float(input("Enter the annual interest rate (IY) as a percentage: "))
        N = float(input("Enter the number of years (N): "))
        compound_frequency = int(input("Enter the number of times interest is compounded per year: "))

        PV = calculate_PV(FV, IY, N, compound_frequency)
        print(f"The present value (PV) of your investment is: ${PV:.2f}")

    elif choice == 3:
        PV = float(input("Enter the Present Value (PV): "))
        IY = float(input("Enter the annual interest rate (IY) as a percentage: "))
        N = float(input("Enter the number of years (N): "))

        PMT = calculate_PMT(PV, IY, N)
        print(f"The payment (PMT) for your investment is: ${abs(PMT):.2f}")

    elif choice == 4:
        PV = float(input("Enter the Present Value (PV): "))
        IY = float(input("Enter the annual interest rate (IY) as a percentage: "))
        PMT = float(input("Enter the payment (PMT): "))

        N = calculate_N(PV, IY, PMT)
        print(f"The number of years (N) for your investment is: {N:.2f}")

    elif choice == 5:
        PV = float(input("Enter the Present Value (PV): "))
        FV = float(input("Enter the future value (FV): "))
        N = float(input("Enter the number of years (N): "))

        IY = calculate_IY(PV, FV, N)
        print(f"The annual interest rate (IY) for your investment is: {IY:.2f}%")

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
