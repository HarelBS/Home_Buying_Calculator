from CostTable import CostTable
import argparse
import os

class HomeCalculator:
    def __init__(
        self,
        years,
        capital,
        purchase_cost,
        monthly_maintenance,
        rent,
        rent_increase,
        alternative_investment_increase,
        property_value,
        property_value_increase,
        interest_rate,
    ):
        # Convert years to integer to ensure consistency
        self.years = int(years)
        self.capital = capital
        self.purchase_cost = purchase_cost
        self.monthly_maintenance = monthly_maintenance
        self.rent = rent
        self.rent_increase = rent_increase
        self.alternative_investment_increase = alternative_investment_increase
        self.property_value = property_value
        self.property_value_increase = property_value_increase
        self.interest_rate = interest_rate
        self.mortgage = property_value + purchase_cost - capital
        self.monthly_payment = self.monthly_mortgage(self.mortgage, self.interest_rate / 100, self.years)
        self.cost_table = CostTable(
            years=self.years,
            capital=self.capital,
            monthly_mortgage=self.monthly_payment,
            monthly_maintenance=self.monthly_maintenance,
            rent=self.rent,
            rent_increase=self.rent_increase,
            alternative_investment_increase=self.alternative_investment_increase
        )

    def monthly_mortgage(self,  loan_amount, interest_rate, years):
        r = interest_rate / 12 # monthly interest rate
        n = years * 12 # number of months / total payments
        return loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    
    def print_header(self):
        """Print a beautiful header for the calculator"""
        print("\n" + "="*70)
        print("🏠  HOME BUYING vs RENTING COST COMPARISON CALCULATOR  🏠")
        print("="*70)
    
    def print_section_header(self, title):
        """Print a section header with decorative elements"""
        print(f"\n{'─'*20} {title} {'─'*20}")
    
    def print_mortgage(self):
        self.print_section_header("📊 MORTGAGE DETAILS")
        
        print(f"📅  Loan Term:           {self.years} years")
        print(f"💳  Monthly Payment:     ${self.monthly_payment:>12,.2f}")
        print(f"💰  Total Payments:      ${self.monthly_payment * self.years * 12:>12,.2f}")
        print(f"💸  Total Interest:      ${self.monthly_payment * self.years * 12 - self.mortgage:>12,.2f}")
        print(f"🏦  Principal Amount:    ${self.mortgage:>12,.2f}")
        print(f"📈  Interest Rate:       {self.interest_rate:>12.2f}%")

    def print_input(self):
        self.print_section_header("📋 INPUT PARAMETERS")
        
        # Create two columns for better layout
        left_col = [
            f"📅  Years:                    {self.years}",
            f"💰  Capital/Down Payment:     ${self.capital:>12,.2f}",
            f"🏠  Property Value:           ${self.property_value:>12,.2f}",
            f"💳  Interest Rate:            {self.interest_rate:>12.2f}%",
            f"📈  Property Value Increase:  {self.property_value_increase:>12.2f}%"
        ]
        
        right_col = [
            f"💸  Purchase Costs:           ${self.purchase_cost:>12,.2f}",
            f"🔧  Monthly Maintenance:      ${self.monthly_maintenance:>12,.2f}",
            f"🏠  Monthly Rent:             ${self.rent:>12,.2f}",
            f"📈  Rent Increase:            {self.rent_increase:>12.2f}%",
            f"📊  Alt. Investment Return:   {self.alternative_investment_increase:>12.2f}%"
        ]
        
        # Print in two columns
        for i in range(max(len(left_col), len(right_col))):
            left = left_col[i] if i < len(left_col) else ""
            right = right_col[i] if i < len(right_col) else ""
            print(f"{left:<40} {right}")

    def print_output(self):
        property_future_value = self.property_value * (1 + self.property_value_increase / 100) ** (self.years)
        total_investment_worth_at_end = self.cost_table.total_investment_value()
        
        self.print_section_header("📊 ANALYSIS RESULTS")
        
        # Buying Scenario
        print("🏠  BUYING SCENARIO:")
        print(f"    💰  Total Buying Cost:      ${self.cost_table.total_buying_cost():>12,.2f}")
        print(f"    📈  Property Future Value:  ${property_future_value:>12,.2f}")
        print(f"    📊  Net Worth:              ${property_future_value - self.cost_table.total_buying_cost():>12,.2f}")
        
        print()
        
        # Renting Scenario
        print("🏠  RENTING SCENARIO:")
        print(f"    💸  Total Rent Paid:        ${self.cost_table.total_rent_paid():>12,.2f}")
        print(f"    📈  Investment Worth:       ${total_investment_worth_at_end:>12,.2f}")
        print(f"    📊  Net Worth:              ${total_investment_worth_at_end:>12,.2f}")
        
        print()
        print("🎯  RECOMMENDATION:")
        print("─" * 50)

        diff = property_future_value - total_investment_worth_at_end
        if diff > 0:
            print("✅  RECOMMENDATION: BUY")
            print(f"    💡  You would be ${diff:,.2f} better off buying")
        else:
            print("✅  RECOMMENDATION: RENT")
            print(f"    💡  You would be ${abs(diff):,.2f} better off renting")
        
        print(f"    📊  Difference (Buying - Renting): ${diff:,.2f}")
        
        # Add a summary box
        print()
        print("📋  SUMMARY:")
        print("─" * 50)
        buying_net = property_future_value
        renting_net = total_investment_worth_at_end
        print(f"    Buying Net Worth:  ${buying_net:>12,.2f}")
        print(f"    Renting Net Worth: ${renting_net:>12,.2f}")
        print(f"    Difference:        ${diff:>12,.2f}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Home Buying Calculator - Compare buying vs renting costs')
    
    parser.add_argument('--years', type=int, default=10, 
                       help='Number of years to calculate')
    parser.add_argument('--capital', type=float, default=500000,
                       help='Initial capital/down payment amount')
    parser.add_argument('--purchase-cost', type=float, default=110000,
                       help='Additional purchase costs (closing costs, fees, etc.)')
    parser.add_argument('--monthly-maintenance', type=float, default=200,
                       help='Monthly maintenance costs')
    parser.add_argument('--rent', type=float, default=4200,
                       help='Monthly rent amount')
    parser.add_argument('--rent-increase', type=float, default=3,
                       help='Annual rent increase percentage')
    parser.add_argument('--alternative-investment-increase', type=float, default=7,
                       help='Annual alternative investment return percentage')
    parser.add_argument('--property-value', type=float, default=1600000,
                       help='Property value/purchase price')
    parser.add_argument('--property-value-increase', type=float, default=4.5,
                       help='Annual property value increase percentage')
    parser.add_argument('--interest-rate', type=float, default=5,
                       help='Annual mortgage interest rate percentage')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    calculator = HomeCalculator(
        years=args.years,
        capital=args.capital,
        purchase_cost=args.purchase_cost,
        monthly_maintenance=args.monthly_maintenance,
        rent=args.rent,
        rent_increase=args.rent_increase,
        alternative_investment_increase=args.alternative_investment_increase,
        property_value=args.property_value,
        property_value_increase=args.property_value_increase,
        interest_rate=args.interest_rate
    )
    
    calculator.print_header()
    calculator.print_input() 
    calculator.print_mortgage()
    calculator.print_output()

if __name__ == "__main__":
    main()