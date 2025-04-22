# https://github.com/confluentinc/confluent-kafka-python 라이브러리 설치
# python -m venv venv / source venv/bin/activate
# 로 가상환경 설정 후 다운로드

# pip install confluent-kafka

from confluent_kafka import Producer
import time
import requests #웹으로 요청보내는 라이브러리로 (venv 가상환경이 설치된 환경에서 터미널에 `pip install requests`로 설치)


# UPBIT_URL = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'
UPBIT_URL = 'https://api.upbit.com/v1/ticker'
params = {
    'markets': 'KRW-BTC'
}


conf = {
    'bootstrap.servers': 'localhost:9092',
}

p = Producer(conf)

while True:
    res = requests.get(UPBIT_URL, params=params)
    bit_data = res.json()[0] #리스트 형태에서 데이터를 가져오려고 [0]을 붙임
    result = f"{bit_data['market']}, {bit_data['trade_date']}, {bit_data['trade_time']}, {bit_data['trade_price']}"
    print(result)
    p.poll(0)
    p.produce('temp', result)
    p.flush()
    time.sleep(5)