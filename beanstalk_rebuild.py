import boto3
def lambda_handler(event, context):
    envid=['#']
    client = boto3.client('elasticbeanstalk')
    try:
         for appid in range(len(envid)):
             response = client.rebuild_environment(EnvironmentId=str(envid[appid].strip()))
             if response:
                 print('Restore environment %s' %str(envid[appid]))
             else:
                 print('Failed to Restore environment %s' %str(envid[appid]))

    except Exception as e:
        print(e)