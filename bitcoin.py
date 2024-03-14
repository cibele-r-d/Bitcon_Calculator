import sys
import requests

def get_data():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)    
        
def get_bitcoin_rate(currency):
    data = get_data()
    try:
        rate = data["bpi"][currency]["rate_float"]
    except KeyError:
        print("Error: Unexpected response format from the API.")
        sys.exit(1)
    return rate


def calculate_bitcoin_price(amount, currency):
    rate = get_bitcoin_rate(currency)
    price = float(rate)*amount
    return price

def get_updated_time():
    data = get_data()
    time = data["time"]["updated"]
    return time



def main():

    
    if len(sys.argv) == 1:
        print(f"In {get_updated_time()} Bitcoin price ${calculate_bitcoin_price(1, "USD")} USD")

    try:
        amount = float(sys.argv[1])
    
        if len(sys.argv) == 2:
            print(f" In {get_updated_time()} {amount} bitcoin(s) price ${calculate_bitcoin_price(amount, "USD")} USD")
    
        elif len(sys.argv) >= 3:
            currency = sys.argv[2].upper()
            if currency not in ["USD", "GBP", "EUR"]:
                print("Invalid currency. Supported currencies: USD, GBP, EUR")
                sys.exit(1)

            elif currency == "USD":
                print(f" In {get_updated_time()} {amount} bitcoin(s) price ${calculate_bitcoin_price(amount, currency)} USD")

            elif currency == "GBP":
                print(f" In {get_updated_time()} {amount} bitcoin(s) price £{calculate_bitcoin_price(amount, currency)} GBP")

            elif currency == "EUR":
                print(f" In {get_updated_time()} {amount} bitcoin(s) price  €{calculate_bitcoin_price(amount, currency)} EUR")



    except ValueError:
        print("Amount must be a valid number.")
        sys.exit(1)

if __name__ == "__main__":          
    main()


