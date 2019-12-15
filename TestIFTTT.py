import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response=requests.get(bitcoin_api_url)

response_json=response.json()

print(response_json[0])


ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/dghSphf4cnhM88yU_s2-v9'
requests.post(ifttt_webhook_url)
