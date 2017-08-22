import pika
import sys
import time

ipServidorRabbit = sys.argv[1]

#connection = pika.BlockingConnection(pika.ConnectionParameters(
#    host = ipServidorRabbit ))

credentials = pika.PlainCredentials('jobson', '123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               ipServidorRabbit, 5672, 'futebol', credentials))

channel = connection.channel()
channel.exchange_declare(exchange='amq.topic',
                 type='topic', durable=True)

arqent = open(sys.argv[2],"r")
n_salto = int(sys.argv[3])

cont = 1

while True:
        linha1 = arqent.readline()
        if linha1 == "":
                break
        if (cont % n_salto == 0):
            lista1 = linha1.split(",")
	    idS = int(lista1[0]);
	    ts = int(lista1[1]);
	    xx = int(lista1[2]);
	    yy = int(lista1[3]);	
            message = "%r,%r,%r,%r" % (idS,ts,xx,yy)
            channel.basic_publish(exchange='amq.topic',
                                      routing_key='hello',
                                      body=message)
            print " [x] Sent %r" % message
            print "*******************************"
            time.sleep(1)
        cont += 1

connection.close()
