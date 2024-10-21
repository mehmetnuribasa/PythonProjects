import requests
import json

api_key = "704759d3605bfb5bb963c849"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
currencyCodes = []  #Holds all currency codes.

#Gets all currency codes..
all_currency_codes = requests.get(api_url + "USD")
json_ACC = json.loads(all_currency_codes.text)

currencyCodes = list(json_ACC["conversion_rates"].keys())

#Gets the information..
while True:
    exchangedCurrency = input("Type of currency exchanged: ")   #USD
    if not exchangedCurrency in currencyCodes:
        print("Invalid Input! Select from the below.")
        print(currencyCodes)
    else:
        break

while True:
    receivedCurrency = input("Type of currency received: ") #TRY
    if not receivedCurrency in currencyCodes:
        print("Invalid Input! Select from the below.")
        print(currencyCodes)
    else:
        break

while True:
    try:
        amount = int(input(f"How much {exchangedCurrency} do you want to exchange: "))
    except Exception as e:
        print(e)
    else:
        break


result = requests.get(api_url + exchangedCurrency)
# print(result.text)

result_json = json.loads(result.text)
# print(result_json["conversion_rates"][receivedCurrency])

print("1 {} = {} {}".format(exchangedCurrency, result_json["conversion_rates"][receivedCurrency], receivedCurrency))
print("{} {} = {} {}".format(amount, exchangedCurrency, amount * result_json["conversion_rates"][receivedCurrency], receivedCurrency))