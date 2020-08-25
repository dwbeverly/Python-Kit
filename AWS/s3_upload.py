import os
import sys
import boto3

#Pass file in same directory as script into file_directory variable
#Change whatever.zip to the filename you want to upload
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file_name = '\\whatever.zip'
file_directory = __location__ + file_name
bucket_name = 'bucket.name'
#Depending on the context, you can change the object name to populate from a cmd line argument, and then just update file_name from that.
object_name = 'whatever.zip'

###################################
#   Upload file to an S3 bucket   #
###################################
def s3_upload():
    s3 = boto3.resource('s3')
    s3.Object("{bucket_name}","{object_name}").upload_file(Filename="{file_directory}")