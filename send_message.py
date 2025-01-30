import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/484666827606/lucas'

# Send message to SQS queue
def send_messages(number_of_messages):
    for i in range(number_of_messages):
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=0,
            MessageBody=(
                'Hello world, im sending messages to queue'
            )
        )
        print(f'sending the {i}° message with the id {response['MessageId']}')



send_messages(200)