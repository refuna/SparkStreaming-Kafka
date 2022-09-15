from kafka import KafkaProducer
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import json
import sys

# import os
# os.environ['HADOOP_HOME'] = 'C:\Hadoop'
# os.environ['SPARK_HOME'] = 'C:\Spark\spark-3.3.0-bin-hadoop3'
# os.environ["JAVA_HOME"] = 'C:\Program Files\Java\jdk-18.0.2'
 
def KafkaWordCount(topics, numThreads):
    sc = SparkContext(appName="StructuredKafkaWordCount")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)

    ssc.checkpoint("./kafka/checkpoint")

    topicAry = topics.split(",")

    topicMap = {}
    for topic in topicAry:
        topicMap[topic] = numThreads
    
    lines = ssc.socketTextStream("localhost", int(2181))
    words = lines.flatMap(lambda x : x.split(" "))
    wordcount = words.map(lambda x : (x, 1)).reduceByKeyAndWindow((lambda x,y : x+y), (lambda x,y : x-y), 1, 1, 1)
    wordcount.foreachRDD(lambda x : sendmsg(x))
    ssc.start()
    ssc.awaitTermination()
 
def Get_dic(rdd_list):
    res = []
    for elm in rdd_list:
        tmp = {elm[0]: elm[1]}
        res.append(tmp)
    return json.dumps(res)
 
def sendmsg(rdd):
    if rdd.count != 0:
        msg = Get_dic(rdd.collect())
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send("result", msg.encode('utf8'))
        producer.flush() 
 
if __name__ == '__main__':
    topics = sys.argv[1]
    numThreads = int(sys.argv[2])
    print(topics, numThreads)
    KafkaWordCount(topics, numThreads)
 