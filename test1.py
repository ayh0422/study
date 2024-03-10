# requests 모듈 설치 필요 (pip install requests)
import requests
import json
import datetime
import time
import yaml
import os
os.chdir("study")
print(os.getcwd())


with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
APP_KEY = _cfg['APP_KEY']
APP_SECRET = _cfg['APP_SECRET']
ACCESS_TOKEN = ""
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
DISCORD_WEBHOOK_URL = _cfg['DISCORD_WEBHOOK_URL']
URL_BASE = _cfg['URL_BASE']


def get_access_token():
    """토큰 발급"""
    headers = {"content-type":"application/json"}
    body = {"grant_type":"client_credentials",
    "appkey":APP_KEY, 
    "appsecret":APP_SECRET}
    PATH = "oauth2/tokenP"
    URL = f"{URL_BASE}/{PATH}"
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    ACCESS_TOKEN = res.json()["access_token"]
    return ACCESS_TOKEN
    
ACCESS_TOKEN = get_access_token()



# url = 'https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/trading/order-cash'
# body = {
#     "CANO": "종합계좌번호",
#     "ACNT_PRDT_CD": "계좌상품코드",
#     "PDNO": "상품번호",
#     "ORD_DVSN": "주문구분",
#     "ORD_QTY": "주문수량",
#     "ORD_UNPR": "주문단가",
#     "CTAC_TLNO": "연락전화번호"
# }
# headers = {
#     "Content-Type": "application/json",
#     "authorization": "Bearer {TOKEN}",
#     "appKey": "{Client_ID}",
#     "appSecret": "{Client_Secret}",
#     "personalSeckey": "{personalSeckey}",
#     "tr_id": "TTTC0802U",
#     "tr_cont": " ",
#     "custtype": "법인(B), 개인(P)",
#     "seq_no": "법인(01), 개인( )",
#     "mac_address": "{Mac_address}",
#     "phone_num": "P01011112222",
#     "ip_addr": "{IP_addr}",
#     "hashkey": "{Hash값}",
#     "gt_uid": "{Global UID}"
# }

# res = requests.post(url, data=json.dumps(body), headers=headers)
# rescode = res.status_code
# if rescode == 200:
#     print(res.headers)
#     print(str(rescode) + " | " + res.text)
# else:
#     print("Error Code : " + str(rescode) + " | " + res.text)
                            