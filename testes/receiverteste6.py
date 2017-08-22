#!/usr/bin/env python
import sys
import pika
#import MySQLdb
import mysql.connector

#con = mysql.connector.connect(user='root',password='admin123',host='localhost',database='dbfutebol')
con = mysql.connector.connect(user='admin',password='admin123',host='52.89.114.226',database='dbfutebol')
cursor = con.cursor()

'''conexao = MySQLdb.connect('localhost', 'root', 'admin123')
conexao.select_db('dbfutebol')
cursor = conexao.cursor()'''

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
   #sql = "INSERT INTO `dbfutebol`.`grid_str` (`idsensor`, `linha`, `coluna`, `celula`) VALUES ('31','33','36','38'); "
   #sql = "insert into grid_str (idsensor, linha, coluna, celula) values (%s, %s, %s, %s)" % ( lista[0], lista[1], lista[2], lista[3] )
   #arg = ( int(lista[0]), int(lista[1]), int(lista[2]), int(lista[3]) )
   #cursor.execute(sql)
   
   #try:
   cursor.execute("""INSERT INTO grid (id, idsensor, linha, coluna, celula) VALUES (null,%s,%s,%s,%s)"""%(lista[0], lista[1], lista[2], lista[3] ) )
   print cursor
   con.commit()
   
   #except MySQLdb.ProgrammingError:
   #print "The following query failed:"
   #print sql

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
