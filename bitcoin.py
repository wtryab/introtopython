import sys
import requests
import json

try:
    num=float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
else:
    try:
        dictionary=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        dictionary=str(dictionary["bpi"]["USD"]["rate"]).replace(",","")
        price=float(dictionary)*num
        print(f"${price:,}")
    except requests.RequestException:
        pass

