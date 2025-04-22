from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'upbit-consumer',
}

c = Consumer(conf)
c.subscribe(['temp'])

try:
    while True:
        msg = c.poll(1)
        
        if msg == None:
            continue
        
        # result = str(msg.value())
        result = msg.value().decode('utf-8')

        print(result)
except KeyboardInterrupt:
    c.close()

print('--end--')