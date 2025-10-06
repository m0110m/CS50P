import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=254cd3ca9ebcc81fb97d8068f37dea5505440c1603bb41cfaa5f9f86358f565b")
    o = response.json()
    data = o["data"]
    value = float(data["priceUsd"])
    amount = value * float(sys.argv[1])
    print(f"${amount:,.4f}")
except (ValueError,requests.RequestException):
    sys.exit("Command-line argument is not a number")
