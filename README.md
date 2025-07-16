# 🏠 Home Buying vs Renting Calculator

A comprehensive calculator to compare the financial implications of buying vs renting a home over time.

## Features

- **Interactive GUI**: Modern, user-friendly interface with input fields for all parameters
- **Real-time Calculations**: Instant results with visual charts
- **Comprehensive Analysis**: Detailed breakdown of costs, mortgage details, and recommendations
- **Visual Charts**: Interactive graphs showing cost comparison over time
- **Tooltips**: Helpful hints for each input parameter

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Note**: `tkinter` is usually included with Python installations, but if you encounter issues:
   - **Windows**: Should be included by default
   - **macOS**: Install with `brew install python-tk`
   - **Linux**: Install with `sudo apt-get install python3-tkinter`

## Usage

### GUI Version (Recommended)
Run the graphical interface:
```bash
python HomeCalculatorGUI.py
```

### Command Line Version
Run the original command-line version:
```bash
python HomeCalculator.py
```

With custom parameters:
```bash
python HomeCalculator.py --years 15 --capital 600000 --property-value 2000000 --interest-rate 4.5
```

## Input Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| **Years** | Number of years to calculate | 10 |
| **Capital/Down Payment** | Initial capital/down payment amount | $500,000 |
| **Property Value** | Property value/purchase price | $1,600,000 |
| **Purchase Costs** | Additional purchase costs (closing costs, fees, etc.) | $110,000 |
| **Monthly Maintenance** | Monthly maintenance costs | $200 |
| **Monthly Rent** | Monthly rent amount | $4,200 |
| **Rent Increase** | Annual rent increase percentage | 3% |
| **Alt. Investment Return** | Annual alternative investment return percentage | 7% |
| **Property Value Increase** | Annual property value increase percentage | 4.5% |
| **Interest Rate** | Annual mortgage interest rate percentage | 5% |

## Output

The calculator provides:

1. **Input Summary**: All parameters used in the calculation
2. **Mortgage Details**: Monthly payment, total payments, interest paid
3. **Cost Analysis**: 
   - Total buying costs vs renting costs
   - Property future value vs investment value
   - Net worth comparison
4. **Recommendation**: Whether buying or renting is financially better
5. **Visual Chart**: Interactive graph showing cost trends over time

## Files

- `HomeCalculatorGUI.py` - Main GUI application
- `HomeCalculator.py` - Original command-line calculator
- `CostTable.py` - Core calculation logic
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Example Output

```
🏠  HOME BUYING vs RENTING COST COMPARISON CALCULATOR  🏠
======================================================================

───────────────── 📋 INPUT PARAMETERS ─────────────────
📅  Years:                    10
💰  Capital/Down Payment:     $   500,000.00
🏠  Property Value:           $ 1,600,000.00
💳  Interest Rate:               5.00%
📈  Property Value Increase:     4.50%
💸  Purchase Costs:           $   110,000.00
🔧  Monthly Maintenance:      $       200.00
🏠  Monthly Rent:             $     4,200.00
📈  Rent Increase:               3.00%
📊  Alt. Investment Return:      7.00%

───────────────── 📊 MORTGAGE DETAILS ─────────────────
📅  Loan Term:           10 years
💳  Monthly Payment:     $   10,000.00
💰  Total Payments:      $  1,200,000.00
💸  Total Interest:      $    200,000.00
🏦  Principal Amount:    $  1,000,000.00
📈  Interest Rate:           5.00%

───────────────── 📊 ANALYSIS RESULTS ─────────────────
🏠  BUYING SCENARIO:
    💰  Total Buying Cost:      $  1,200,000.00
    📈  Property Future Value:  $  2,400,000.00
    📊  Net Worth:              $  1,200,000.00

🏠  RENTING SCENARIO:
    💸  Total Rent Paid:        $    600,000.00
    📈  Investment Worth:       $  1,000,000.00
    📊  Net Worth:              $  1,000,000.00

🎯  RECOMMENDATION:
──────────────────────────────────────────────────
✅  RECOMMENDATION: BUY
    💡  You would be $200,000 better off buying
    📊  Difference (Buying - Renting): $200,000
```

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the calculator!

## License

This project is open source and available under the MIT License. 