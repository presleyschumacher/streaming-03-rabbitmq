"""
This program will receive messages from the queue and print them.

Presley Schumacher
January 31 2023
 
Approach
---------
Simple - one producer / one consumer.

Since this process runs continuously, 
if we want to emit more messages, 
we'll need to open a new terminal window.

Terminal Reminders
------------------

- Use Control c to close a terminal and end a process.

- Use the up arrow to get the last command executed.

"""

# you can add multiple imports on one line 
# but we don't recommend it for readability
import pika, sys, os

# define a main function to run the program
def main():
    # Establish a connection with RabbitMQ Server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='LocalHost'))
    channel = connection.channel()
    # Create a hello queue to which the message(s) will be delievered
    channel.queue_declare(queue='hello')
    # Subscribe a callback function to a queue which is called by the Pika library and will print the contents of the message
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
    # Tell RabbitMQ that the callback function should receive message from the hello queue
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    # Print the message
    print(' [*] Waiting for messages. To exit press CTRL+C')
    # Start consuming messages
    channel.start_consuming()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)