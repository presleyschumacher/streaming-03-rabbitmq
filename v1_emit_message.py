"""
    This program sends a message to a queue on the RabbitMQ server.

    Presley Schumacher
    January 31, 2023

"""

# add imports at the beginning of the file
import pika

#The first program, send.py, will send a single message to the queue.

# Establish a connection with RabbitMQ Server
conn = pika.BlockingConnection(pika.ConnectionParameters('LocalHost'))
ch = conn.channel()
# Now we're connnected to a broker on the local machine.
# Before sending a message, we need to make sure the recipient queue exists
# We will create a hello queue to which the message(s) will be delivered
ch.queue_declare(queue="hello")
# We are ready to send our first message
# In RabbitMQ, the message goes through an exchange before being sent to the queue.
# We will use the default exchange identified by an empty string. The queue name is specified in the routing_key parameter 
ch.basic_publish(exchange="", routing_key="hello", body="Hello World!")
# Print the message
print(" [x] Sent 'Hello World!'")
# Close the connection
conn.close()
