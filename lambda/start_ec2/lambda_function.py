import os
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    instance_ids = os.environ['INSTANCE_IDS'].split(',')
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    
    try:
        ec2.start_instances(InstanceIds=instance_ids)
        print(f'Successfully started instances: {instance_ids}')
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=f'Successfully started instances: {instance_ids}',
            Subject='EC2 Instances Started'
        )
    except Exception as e:
        print(f'Error starting instances: {e}')
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=f'Error starting instances: {e}',
            Subject='EC2 Instances Starting Error'
        )

