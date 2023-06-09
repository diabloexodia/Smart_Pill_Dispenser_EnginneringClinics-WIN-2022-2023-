#Author - @Diabloexodia[13042023-11:13]

import boto3


#------------------------------------------ AWS Fetch-[DO NOT TAMPER]---------------------------------------------------
# Create an S3 client with your AWS credentials
s3 = boto3.client('s3',
                  aws_access_key_id='YOUR-ACCESS-KEY',
                  aws_secret_access_key='YOUR-SECRET-KEY',
region_name='ap-southeast-1')

# Set the name of the S3 bucket and object key of the text file you want to display
bucket_name = 'smartpills'
object_key = 'userdetails/userdetails.txt'

# Download the text file from the S3 bucket to a local file path on the Raspberry Pi
local_file_path = 'home/pi/Downloads/text_file.txt'
s3.download_file(bucket_name, object_key, local_file_path)

# Read the contents of the text file
with open(local_file_path, 'r') as f:
    file_contents = f.read()

#-----------------------------------------------------------------------------------------------------------------------

# Display the contents of the text file on the Raspberry Pi output
print(file_contents)


# TODO - Code for dispensing functionality 
