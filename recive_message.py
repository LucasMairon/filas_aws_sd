import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/484666827606/lucas'

def receive_and_delete_messages(number_of_messages):
    for i in range(number_of_messages):
        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        messages = response['Messages']
        for message in messages:
            receipt_handle = message['ReceiptHandle']
            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            print('Received and deleted message: %s' % message)

    print(f'Total of messages consumed: {i}')

receive_and_delete_messages(200)
