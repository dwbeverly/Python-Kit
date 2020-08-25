import os
import sys
import boto3

#note - instance ID has to be in an array since that's what boto3 is expecting for subsequent calls
#I use this in conjunction with the get_ec2_ids function
EC2_INSTANCE_ID = []

###################################
#      Start EC2 using Boto3      #
###################################

def start_ec2():
    ec2client = boto3.client('ec2')
    response = ec2client.start_instances(InstanceIds=EC2_INSTANCE_ID)