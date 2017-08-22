#!/usr/bin/env python
import sys
import pika
#import MySQLdb
import mysql.connector

con = mysql.connector.connect(user='root',password='admin123',host='localhost',database='dbfutebol')
cursor = con.cursor()

ipServidorRabbit = sys.argv[1]

credentials = pika.PlainCredentials('jobson', '123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
   ipServidorRabbit, 5672, 'futebol', credentials))

channel = connection.channel()

channel.exchange_declare(exchange='top.futebol',
                         type='topic')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

binding_keys = "*"

channel.queue_bind(exchange='top.futebol',
                  queue=queue_name,
                  routing_key=binding_keys)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
   body = body.split(" ")
   print (body)
   inserirBanco(cursor, body)

def inserirBanco(cursor, lista):
   cursor.execute("""INSERT INTO grid (id, idsensor, linha, coluna, celula) VALUES (null,%s,%s,%s,%s)"""%(lista[0], lista[1], lista[2], lista[3] ) )
   con.commit()
   
channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
