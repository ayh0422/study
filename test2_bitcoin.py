
import requests

def get_bitcoin_price_krw():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=krw"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["krw"]
    return price

# 비트코인 현재 가격(한국 원) 출력
print(f"Bitcoin current price: ₩ {get_bitcoin_price_krw():,}")

from slacker import Slacker

slack = Slacker('xoxb-6776949886388-6759940371367-bVzvoqMKEHlSnyasfDqek0Vx')

# Send a message to #general channel
slack.chat.post_message('#bitcoint-test', 'Hello fellow slackers!')
