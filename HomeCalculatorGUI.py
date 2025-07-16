import tkinter as tk
from tkinter import ttk, messagebox
from HomeCalculator import HomeCalculator
import threading

class HomeCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏠 Home Buying vs Renting Calculator")
        
        # Get screen dimensions and calculate responsive sizes
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Calculate responsive dimensions
        self.window_width = min(int(self.screen_width * 0.9), 1800)
        self.window_height = min(int(self.screen_height * 0.85), 1200)
        
        # Calculate responsive font sizes
        self.title_font_size = max(16, int(self.screen_width / 60))
        self.header_font_size = max(12, int(self.screen_width / 80))
        self.normal_font_size = max(10, int(self.screen_width / 100))
        self.button_font_size = max(12, int(self.screen_width / 80))
        self.frame_title_font_size = max(14, int(self.screen_width / 70))
        
        # Set window size and position
        x = (self.screen_width - self.window_width) // 2
        y = (self.screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.root.configure(bg='#f0f0f0')
        
        # Set style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables to store input values
        self.vars = {}
        self.setup_variables()
        self.create_widgets()
        
        # Bind window resize event
        self.root.bind('<Configure>', self.on_window_resize)
        
    def setup_variables(self):
        """Initialize all input variables with default values"""
        self.vars = {
            'years': tk.DoubleVar(value=10),
            'capital': tk.DoubleVar(value=500000),
            'purchase_cost': tk.DoubleVar(value=110000),
            'monthly_maintenance': tk.DoubleVar(value=200),
            'rent': tk.DoubleVar(value=4200),
            'rent_increase': tk.DoubleVar(value=3),
            'alternative_investment_increase': tk.DoubleVar(value=7),
            'property_value': tk.DoubleVar(value=1600000),
            'property_value_increase': tk.DoubleVar(value=4.5),
            'interest_rate': tk.DoubleVar(value=5)
        }
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for better responsive layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)  # Input column
        main_frame.columnconfigure(1, weight=1)  # Results column 1
        main_frame.columnconfigure(2, weight=1)  # Results column 2
        main_frame.rowconfigure(1, weight=1)     # Results row
        
        # Title
        title_label = ttk.Label(main_frame, text="🏠 Home Buying vs Renting Calculator", 
                               font=('Arial', self.title_font_size, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Create input section
        self.create_input_section(main_frame)
        
        # Create results sections (split into columns)
        self.create_results_section(main_frame)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to calculate")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W, font=('Arial', self.normal_font_size))
        status_bar.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def create_input_section(self, parent):
        """Create the input parameters section"""
        # Input frame
        input_frame = ttk.LabelFrame(parent, text="📋 Input Parameters", padding="20")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 15))
        
        # Configure frame title font
        self.style.configure('TLabelframe.Label', font=('Arial', self.frame_title_font_size, 'bold'))
        
        # Input fields
        inputs = [
            ("📅 Years:", 'years', "Number of years to calculate"),
            ("💰 Capital/Down Payment ($):", 'capital', "Initial capital/down payment amount"),
            ("🏠 Property Value ($):", 'property_value', "Property value/purchase price"),
            ("💸 Purchase Costs ($):", 'purchase_cost', "Additional purchase costs (closing costs, fees, etc.)"),
            ("🔧 Monthly Maintenance ($):", 'monthly_maintenance', "Monthly maintenance costs"),
            ("🏠 Monthly Rent ($):", 'rent', "Monthly rent amount"),
            ("📈 Rent Increase (%):", 'rent_increase', "Annual rent increase percentage"),
            ("📊 Alt. Investment Return (%):", 'alternative_investment_increase', "Annual alternative investment return percentage"),
            ("📈 Property Value Increase (%):", 'property_value_increase', "Annual property value increase percentage"),
            ("💳 Interest Rate (%):", 'interest_rate', "Annual mortgage interest rate percentage")
        ]
        
        for i, (label_text, var_name, tooltip) in enumerate(inputs):
            # Label
            label = ttk.Label(input_frame, text=label_text, font=('Arial', self.normal_font_size))
            label.grid(row=i, column=0, sticky=tk.W, pady=8)
            
            # Entry
            entry = ttk.Entry(input_frame, textvariable=self.vars[var_name], width=20, font=('Arial', self.normal_font_size))
            entry.grid(row=i, column=1, padx=(15, 0), pady=8, sticky=tk.W)
            
            # Tooltip
            self.create_tooltip(entry, tooltip)
        
        # Calculate button - placed beneath input parameters
        calculate_btn = ttk.Button(input_frame, text="🔄 Calculate", 
                                  command=self.calculate, style='Accent.TButton')
        calculate_btn.grid(row=len(inputs), column=0, columnspan=2, pady=(20, 0), sticky=(tk.E, tk.W))
        
        # Configure button style for larger text
        self.style.configure('Accent.TButton', font=('Arial', self.button_font_size, 'bold'))
    
    def create_results_section(self, parent):
        """Create the results display section with multiple columns"""
        # Initialize results widgets dictionary
        self.results_widgets = {}
        
        # Create two separate frames for different columns
        # Column 1: Mortgage Details
        col1_frame = ttk.LabelFrame(parent, text="🏦 Mortgage Details", padding="10")
        col1_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(15, 5))
        col1_frame.columnconfigure(0, weight=1)
        col1_frame.rowconfigure(0, weight=1)  # Make it expandable
        self.col1_frame = col1_frame
        
        # Column 2: Cost Comparison, Property Analysis, and Recommendation
        col2_frame = ttk.LabelFrame(parent, text="💰 Costs & Analysis", padding="10")
        col2_frame.grid(row=1, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        col2_frame.columnconfigure(0, weight=1)
        col2_frame.rowconfigure(0, weight=1)  # Make it expandable
        self.col2_frame = col2_frame
        
        # Initial messages
        initial_label1 = ttk.Label(col1_frame, 
                                  text="Click 'Calculate' to see the analysis results...",
                                  font=('Arial', self.normal_font_size))
        initial_label1.grid(row=0, column=0, pady=10)
        self.results_widgets['initial1'] = initial_label1
        
        initial_label2 = ttk.Label(col2_frame, 
                                  text="Click 'Calculate' to see the analysis results...",
                                  font=('Arial', self.normal_font_size))
        initial_label2.grid(row=0, column=0, pady=10)
        self.results_widgets['initial2'] = initial_label2
    
    def create_tooltip(self, widget, text):
        """Create a tooltip for a widget"""
        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(tooltip, text=text, justify=tk.LEFT,
                           background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                           font=('Arial', self.normal_font_size))
            label.pack()
            
            def hide_tooltip():
                tooltip.destroy()
            
            widget.tooltip = tooltip
            widget.bind('<Leave>', lambda e: hide_tooltip())
        
        widget.bind('<Enter>', show_tooltip)
    
    def calculate(self):
        """Perform the calculation in a separate thread"""
        self.status_var.set("Calculating...")
        self.root.update()
        
        # Run calculation in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self._calculate_thread)
        thread.daemon = True
        thread.start()
    
    def _calculate_thread(self):
        """Thread function for calculation"""
        try:
            # Get values from variables
            args = {name: var.get() for name, var in self.vars.items()}
            
            # Create calculator instance
            calculator = HomeCalculator(**args)
            
            # Update GUI in main thread
            self.root.after(0, self._update_results, calculator)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Calculation error: {str(e)}"))
            self.root.after(0, lambda: self.status_var.set("Error occurred"))
    
    def _update_results(self, calculator):
        """Update the results display with organized frames in two columns"""
        try:
            # Clear previous results
            for widget in self.results_widgets.values():
                widget.destroy()
            self.results_widgets.clear()
            
            # Get calculation results
            results = self._get_calculation_results(calculator)
            
            # Calculate the key values using the calculator methods
            total_buying_cost = calculator.cost_table.total_buying_cost()
            total_rent_paid = calculator.cost_table.total_rent_paid()
            total_investment_worth = calculator.cost_table.total_investment_value()
            property_future_value = calculator.property_value * (1 + calculator.property_value_increase / 100) ** calculator.years
            
            # COLUMN 1: Mortgage Details
            row1 = 1  # Start at row 1 since row 0 has the calculate button
            
            # Mortgage Details (all the details from terminal output)
            mortgage_amount = calculator.property_value + calculator.purchase_cost - calculator.capital
            monthly_payment = calculator.monthly_payment
            total_payments = monthly_payment * calculator.years * 12
            total_interest = total_payments - mortgage_amount
            
            mortgage_details = [
                f"📅  Loan Term:           {calculator.years} years",
                f"💳  Monthly Payment:     ${monthly_payment:>12,.2f}",
                f"💰  Total Payments:      ${total_payments:>12,.2f}",
                f"💸  Total Interest:      ${total_interest:>12,.2f}",
                f"🏦  Principal Amount:    ${mortgage_amount:>12,.2f}",
                f"📈  Interest Rate:       {calculator.interest_rate:>12.2f}%"
            ]
            
            for i, text in enumerate(mortgage_details):
                label = ttk.Label(self.col1_frame, text=text, font=('Arial', self.normal_font_size))
                label.grid(row=row1 + i, column=0, sticky=tk.W, pady=2)
                self.results_widgets[f'mortgage_{i}'] = label
            

            
            # COLUMN 2: Analysis Results (matching terminal exactly)
            row2 = 0
            
            # 1. Buying Scenario Frame
            buying_frame = ttk.LabelFrame(self.col2_frame, text="🏠 BUYING SCENARIO", padding="10")
            buying_frame.grid(row=row2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
            buying_frame.columnconfigure(0, weight=1)
            row2 += 1
            
            buying_net_worth = property_future_value - total_buying_cost
            
            buying_details = [
                f"    💰  Total Buying Cost:      ${total_buying_cost:>12,.2f}",
                f"    📈  Property Future Value:  ${property_future_value:>12,.2f}"
            ]
            
            for i, text in enumerate(buying_details):
                label = ttk.Label(buying_frame, text=text, font=('Arial', self.normal_font_size))
                label.grid(row=i, column=0, sticky=tk.W, pady=2)
                self.results_widgets[f'buying_{i}'] = label
            
            # 2. Renting Scenario Frame
            renting_frame = ttk.LabelFrame(self.col2_frame, text="🏠 RENTING SCENARIO", padding="10")
            renting_frame.grid(row=row2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
            renting_frame.columnconfigure(0, weight=1)
            row2 += 1
            
            renting_details = [
                f"    💸  Total Rent Paid:        ${total_rent_paid:>12,.2f}",
                f"    📈  Investment Worth:       ${total_investment_worth:>12,.2f}"
            ]
            
            for i, text in enumerate(renting_details):
                label = ttk.Label(renting_frame, text=text, font=('Arial', self.normal_font_size))
                label.grid(row=i, column=0, sticky=tk.W, pady=2)
                self.results_widgets[f'renting_{i}'] = label
            
            # 3. Recommendation Frame
            recommendation_frame = ttk.LabelFrame(self.col2_frame, text="🎯 RECOMMENDATION", padding="10")
            recommendation_frame.grid(row=row2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
            recommendation_frame.columnconfigure(0, weight=1)
            row2 += 1
            
            diff = property_future_value - total_investment_worth
            
            if diff > 0:
                recommendation_text = f"✅  RECOMMENDATION: BUY"
                detail_text = f"    💡  You would be ${diff:,.2f} better off buying"
                color = 'green'
            else:
                recommendation_text = f"✅  RECOMMENDATION: RENT"
                detail_text = f"    💡  You would be ${abs(diff):,.2f} better off renting"
                color = 'red'
            
            rec_label = ttk.Label(recommendation_frame, 
                                text=recommendation_text, 
                                font=('Arial', self.normal_font_size, 'bold'),
                                foreground=color)
            rec_label.grid(row=0, column=0, sticky=tk.W, pady=2)
            self.results_widgets['recommendation'] = rec_label
            
            detail_label = ttk.Label(recommendation_frame, 
                                   text=detail_text, 
                                   font=('Arial', self.normal_font_size),
                                   foreground=color)
            detail_label.grid(row=1, column=0, sticky=tk.W, pady=2)
            self.results_widgets['recommendation_detail'] = detail_label
            
            diff_label = ttk.Label(recommendation_frame, 
                                 text=f"    📊  Difference (Buying - Renting): ${diff:,.2f}", 
                                 font=('Arial', self.normal_font_size))
            diff_label.grid(row=2, column=0, sticky=tk.W, pady=2)
            self.results_widgets['recommendation_diff'] = diff_label
            
            self.status_var.set("Calculation completed successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error updating results: {str(e)}")
            self.status_var.set("Error updating results")
    
    def _create_section_header(self, row, text):
        """Create a section header"""
        header = ttk.Label(self.scrollable_results_frame, text=text, 
                          font=('Arial', self.header_font_size, 'bold'), foreground='#2E86AB')
        header.grid(row=row, column=0, sticky=tk.W, pady=(15, 5))
        self.results_widgets[f'header_{row}'] = header
    
    def _get_calculation_results(self, calculator):
        """Extract calculation results from the calculator"""
        # This method can be expanded to extract more specific results
        # For now, we'll use the cost table data
        return {
            'cost_table': calculator.cost_table.df,
            'years': calculator.years,
            'capital': calculator.capital,
            'property_value': calculator.property_value,
            'rent': calculator.rent
        }
    
    def on_window_resize(self, event):
        """Handle window resize events"""
        # Only handle main window resize, not child widgets
        if event.widget == self.root:
            # Update window dimensions
            self.window_width = event.width
            self.window_height = event.height
            
            # Recalculate font sizes based on new window size
            self.title_font_size = max(16, int(self.window_width / 60))
            self.header_font_size = max(12, int(self.window_width / 80))
            self.normal_font_size = max(10, int(self.window_width / 100))
            self.button_font_size = max(12, int(self.window_width / 80))
            self.frame_title_font_size = max(14, int(self.window_width / 70))
            
            # Update styles
            self.style.configure('Accent.TButton', font=('Arial', self.button_font_size, 'bold'))
            self.style.configure('TLabelframe.Label', font=('Arial', self.frame_title_font_size, 'bold'))

def main():
    root = tk.Tk()
    app = HomeCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 