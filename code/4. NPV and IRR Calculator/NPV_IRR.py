import matplotlib.pyplot as plt

def npv(cash_flows, discount_rate):
    total_npv = 0
    for i, cash_flow in enumerate(cash_flows):
        npv = cash_flow / (1 + discount_rate) ** i
        total_npv += npv
    return total_npv

def irr(cash_flows, max_iterations=1000, tolerance=1e-6):
    lower_bound = -1
    upper_bound = 1

    for _ in range(max_iterations):
        mid = (lower_bound + upper_bound) / 2
        npv_mid = npv(cash_flows, mid)
        
        if abs(npv_mid) < tolerance:
            return mid
        elif npv_mid > 0:
            lower_bound = mid
        else:
            upper_bound = mid

    return None


def plot_cash_flows(ax, cash_flows):
    ax.bar(range(len(cash_flows)), cash_flows)
    ax.set_xlabel("Period")
    ax.set_ylabel("Cash Flow")
    ax.set_title("Cash Flows")

def plot_npv_vs_discount_rate(ax, cash_flows, min_rate, max_rate, num_rates):
    discount_rates = [rate / 100 for rate in range(min_rate, max_rate + 1, (max_rate - min_rate) // num_rates)]
    npv_values = [npv(cash_flows, rate) for rate in discount_rates]
    ax.plot(discount_rates, npv_values)
    ax.set_xlabel("Discount Rate")
    ax.set_ylabel("Net Present Value (NPV)")
    ax.set_title("NPV vs. Discount Rate")


if __name__ == "__main__":
    num_cash_flows = int(input("Enter the number of cash flows: "))
    cash_flows = []

    for i in range(num_cash_flows):
        cash_flow = float(input(f"Enter cash flow {i + 1}: "))
        cash_flows.append(cash_flow)

    discount_rate = float(input("Enter the discount rate as a whole number (e.g., 10 for 10%): "))
    discount_rate /= 100

    npv_result = npv(cash_flows, discount_rate)
    irr_result = irr(cash_flows)

    print(f"Net Present Value (NPV) at {discount_rate * 100}% discount rate: ${npv_result:.2f}")
    
    if irr_result is None:
        print("Internal Rate of Return (IRR) calculation did not converge.")
    else:
        print(f"Internal Rate of Return (IRR): {irr_result * 100:.2f}%")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # Add this line
    plot_cash_flows(axes[0], cash_flows)  # Pass axes[0] as the first argument
    
    min_discount_rate = int(input("Enter the minimum discount rate for NPV plot (e.g., 5 for 5%): "))
    max_discount_rate = int(input("Enter the maximum discount rate for NPV plot (e.g., 25 for 25%): "))
    num_rates = int(input("Enter the number of discount rates to evaluate between the minimum and maximum: "))
    plot_npv_vs_discount_rate(axes[1], cash_flows, min_discount_rate, max_discount_rate, num_rates)  # Pass axes[1] as the first argument

    plt.tight_layout()
    plt.show()