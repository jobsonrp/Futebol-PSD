#!/usr/bin/env python
import pika
import sys
import time

ip_rabbitmq_server = sys.argv[1]

if not ip_rabbitmq_server:
    print >> sys.stderr, "Usage: %s [rabbitmq_server_ip]..." % (sys.argv[0],)
    sys.exit(1)

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               ip_rabbitmq_server, 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

def lista_arquivo():
    linha1, linha2 = [],[]
    while True:
        linha1 = arqent.readline()
        if linha1 == "":
            break
        linha2.append(linha1)
    return linha2

arqent = open(sys.argv[2],"r")
# arqsaida = open(sys.argv[2],"w")
routing_keys = lista_arquivo()
print "lista entrada: %r:%d" % (routing_keys, len(routing_keys))
#print "lista entrada[1][0]+4: %d" % (lista_entrada[1][0]+4)

for i in range(0,len(routing_keys)):
        message = '%d,%d' % (time.time(), i)
        channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_keys[i],
                      body=message)
        print " [x] Sent %r:%r" % (routing_keys[i],message)
        time.sleep(2)
connection.close()

