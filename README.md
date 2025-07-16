# 🏠 Home Buying vs Renting Calculator

A comprehensive calculator to compare the financial implications of buying vs renting a home over time.

## Features

- **Interactive GUI**: Modern, user-friendly interface with input fields for all parameters
- **Real-time Calculations**: Instant results with detailed breakdown
- **Comprehensive Analysis**: Detailed breakdown of costs, mortgage details, and recommendations
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

1. **Mortgage Details**: Monthly payment, total payments, interest paid
2. **Cost Analysis**: 
   - Total buying costs vs renting costs
   - Property future value vs investment value
3. **Recommendation**: Whether buying or renting is financially better

## Files

- `HomeCalculatorGUI.py` - Main GUI application
- `HomeCalculator.py` - Original command-line calculator
- `CostTable.py` - Core calculation logic
- `requirements.txt` - Python dependencies 