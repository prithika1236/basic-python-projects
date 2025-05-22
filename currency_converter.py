# Simple Currency Converter

# Define exchange rates
exchange_rates = {
    'USD': 1.0,  # Base currency
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0,
    'INR': 74.0
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Invalid currency code.")
    
    # Convert amount to USD
    amount_in_usd = amount / exchange_rates[from_currency]
    
    # Convert USD to target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

def main():
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("Enter the currency code you are converting from (USD, EUR, GBP, JPY, INR): ").upper()
    to_currency = input("Enter the currency code you are converting to (USD, EUR, GBP, JPY, INR): ").upper()
    
    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
