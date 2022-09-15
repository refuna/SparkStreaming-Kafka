import csv
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

filename = "./data/user_log.csv"
with open(filename) as file:
    reader = csv.DictReader(file, delimiter=",")
    for line in reader:
        print(line['gender'])
        p.produce('mytopic', (line['gender']).encode('utf-8'), callback=delivery_report)
        p.poll(10) 
        p.flush() 

print()