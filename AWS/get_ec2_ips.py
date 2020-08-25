import os
import sys
import boto3

###################################
# Grab EC2 Public IPs using Boto3 #
###################################

def get_ec2_ips():
    ec2client = boto3.client('ec2')
    #If you have several instances, you can update this with tags to filter
    #format is ec2client.describe_instances(Filters=[{'Name' : 'tag-name','Values' : ['tag-value']}])
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This will store the output value into the array we defined earlier
            EC2_PUBIP = (instance["PublicIpAddress"])