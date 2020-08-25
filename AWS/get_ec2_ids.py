import os
import sys
import boto3

#note - instance ID has to be in an array since that's what boto3 is expecting for subsequent calls
EC2_INSTANCE_ID = []

###################################
#   Grab EC2 IDs using Boto3      #
###################################

def get_ec2_ids():
    ec2client = boto3.client('ec2')
    #If you have several instances, you can update this with tags to filter
    #format is ec2client.describe_instances(Filters=[{'Name' : 'tag-name','Values' : ['tag-value']}])
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This will store the output value into the array we defined earlier
            EC2_INSTANCE_ID.append(instance["InstanceId"])