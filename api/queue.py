import pika


def post_to_provider(json):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='json_data_dump')
	channel.basic_publish(exchange='', routing_key='json_data_dump', body=json)
	connection.close()


def consume_from_queue():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='json_data_dump')
	channel.basic_consume(data_dump_callback, queue='json_data_dump', no_ack=False)

	channel.start_consuming()


def data_dump_callback(ch, method, properties, body):
	print body
