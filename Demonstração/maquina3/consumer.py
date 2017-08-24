#!/usr/bin/env python
import pika
import time
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.mqtt import MQTTUtils

def calculaMx(d1,d2):
   if (d1 == 0):
       incremento = 1
   elif ( int(100*d1/d2) == 100*int(d1/d2) ):
       incremento = 0
   elif (d1 % d2 == 0):
       incremento = 0
   else:
       incremento = 1
   return int(d1/d2) + incremento

def calculaMy(d1,d2):
   if (d1 == 67925):
       incremento = -1
   else:
       incremento = 0
   return int(d1/d2) + incremento

def mapear(linha):
   lista = linha.split(",")
   cX = x_max/pX
   cY = y_max/pY
   sid = int(lista[0])
   x = int(lista[2])
   y = int(lista[3]) + deslocamentoY
   mX = calculaMx(x, cX)
   mY = calculaMy(y, cY)
   nCelula = mY*pX + mX
   nColuna = mX
   nLinha = mY + 1
   lista2 = [sid,nLinha,nColuna,nCelula]
   enviarDadosGrid(lista2)
   return lista2

def splitLinha(linha):
       return linha.split(",")[0]

def calculaGrid(linha):
       parametros = linha.split(",")
       return parametros[0]

def enviarDadosGrid(lista):
   credentials = pika.PlainCredentials('jobson', '123')
   connection = pika.BlockingConnection(pika.ConnectionParameters(
       ipServidorRabbit, 5672, 'futebol', credentials))

   channel = connection.channel()

   channel.exchange_declare(exchange='top.futebol',
                            type='topic')#, durable=True)

   message = str(lista[0]) + " " + str(lista[1]) + " " + str(lista[2]) + " " + str(lista[3])

   channel.basic_publish(exchange='top.futebol',
                         routing_key='hello',
                         body=message)
   print " [x] sent %r" % message
   print "*******************"
   #time.sleep(1)

ipServidorRabbit = sys.argv[1]
pX = int(sys.argv[2])
pY = int(sys.argv[3])

x_min = 0
x_max = 52483
deslocamentoY = 33960
y_min = 0
y_max = 67925 # 33965 + 33960

sc = SparkContext()
ssc = StreamingContext(sc, 10)

lines = MQTTUtils.createStream(
   ssc,
   "tcp://%s:1883" % ipServidorRabbit,  
   "hello"                  
)

counts = lines.map(mapear)

counts.pprint()

ssc.start()
ssc.awaitTermination()
ssc.stop()
