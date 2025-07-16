import pandas as pd

class CostTable:
    def __init__(self, years, capital, monthly_mortgage, monthly_maintenance, rent, rent_increase, alternative_investment_increase):
        # Convert years to integer to avoid float/integer conversion issues
        self.years = int(years)
        self.base_rent = rent
        self.rent_increase = rent_increase / 100
        self.df = pd.DataFrame({
            'buying_cost': [capital] + [(monthly_mortgage + monthly_maintenance) for i in range(1, self.years*12 + 1)],
            'renting_cost': [self.calculate_rent(i) for i in range(0, self.years*12 + 1)],
        }, index=[i for i in range(0, self.years*12 + 1)])
        self.df.index.name = 'month'
        self.df['diff'] = self.df['buying_cost'] - self.df['renting_cost']
        self.df['investment'] = self.df['diff'] * ((1 + alternative_investment_increase / 100) ** (1/12)) ** (self.years*12 - self.df.index)


    def calculate_rent(self, month):
        # Calculate the rent for the given month
        if month <= 0:
            return 0
        year = int((month-1) // 12)  # Ensure year is an integer
        return self.base_rent * (1 + self.rent_increase) ** year
    
    def print_df(self):
        """Print the cost table with beautiful formatting"""
        print("\n" + "─"*80)
        print("📊  DETAILED MONTHLY COST BREAKDOWN")
        print("─"*80)
        
        # Set pandas to display all rows locally for this print only
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.float_format', '{:,.2f}'.format):
            # Rename columns for better display
            display_df = self.df.copy()
            display_df.columns = ['🏠 Buying Cost', '🏠 Renting Cost', '💰 Difference', '📈 Investment Value']
            display_df.index.name = '📅 Month'
            
            print(display_df)
        
        print("\n" + "─"*80)
        print("📋  SUMMARY TOTALS:")
        print("─"*80)
        print(f"💰  Total Buying Cost:     ${self.total_buying_cost():>15,.2f}")
        print(f"🏠  Total Rent Paid:       ${self.total_rent_paid():>15,.2f}")
        print(f"📈  Investment Worth:      ${self.total_investment_value():>15,.2f}")
        print(f"💡  Net Difference:        ${self.total_investment_value() - self.total_rent_paid():>15,.2f}")

    def total_rent_paid(self):
        return self.df['renting_cost'].sum()
    
    def total_buying_cost(self):
        return self.df['buying_cost'].sum()

    def total_investment_value(self):
        return self.df['investment'].sum()
    


if __name__ == "__main__":
    cost_table = CostTable(years=10, capital=500000, monthly_mortgage=10000, monthly_maintenance=100, rent=4000, rent_increase=2, alternative_investment_increase=7)
    cost_table.print_df()
    print(f"Total investment worth at end: {cost_table.total_investment_value():,.2f}")
    print(f"Total rent paid: {cost_table.total_rent_paid():,.2f}")
    print(f"Total buying cost: {cost_table.total_buying_cost():,.2f}")
    


