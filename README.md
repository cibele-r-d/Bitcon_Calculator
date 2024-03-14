# Bitcoin Price Calculator
## Summary:
The Bitcoin Price Calculator is a Python script that retrieves the current bitcoin prices from the Coindesk API and calculates the equivalent value in various currencies based on user input. It provides users with the flexibility to specify the amount of bitcoins and the desired currency, and then displays the calculated price along with the updated time of the API response.

## Features:
- Retrieves current bitcoin prices from the Coindesk API.
- Supports calculation of bitcoin prices in USD, GBP, and EUR.
- Allows users to specify the amount of bitcoins and the desired currency via command-line arguments.
- Displays the calculated price along with the updated time of the API response.
- Provides error handling for invalid inputs and unexpected API responses.
## Usage:
To use the Bitcoin Price Calculator, run the script with the following command-line arguments:
  
  **python bitcoin_calculator.py 'amount' 'currency'**
    
  **amount:** The amount of bitcoins to calculate the price for (optional, default is 1).  
  **currency:** The desired currency (USD, GBP, or EUR).

## Example:
python bitcoin_calculator.py 2 GBP

**Output:**  
In 2024-02-20T17:58:00Z, 2 bitcoin(s) price £1234.56 GBP
