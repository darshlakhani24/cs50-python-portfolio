import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        bitcoins = float(sys.argv[1])
        if bitcoins <= 0:
            raise ValueError
    except ValueError:
        sys.exit("Error: Number of Bitcoins must be a positive number.")

    try:
        url = "https://api.coincap.io/v2/assets/bitcoin"
        headers = {
            "Authorization": "Bearer ef280ab412eb6182cfabb04c9a7c93f51d253545d33bb7d64a5ae5e2bcc2e575"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")
    except (KeyError, ValueError):
        sys.exit("Error: Unexpected response format.")

    total_cost = bitcoins * price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
