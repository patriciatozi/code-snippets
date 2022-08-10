import boto3

file_path = '/tmp/'
file_name = 'hello.txt'

# S3 Bucket info (name/path)
S3_BUCKET_NAME = 's3-bucket-name'
S3_BUCKET_PATH = 's3-bucket-path'

# Create S3 Bucket Session
session = boto3.Session() 
s3 = session.resource('s3')

# How to upload hello.txt to S3 Bucket
result = s3.Bucket(S3_BUCKET_NAME).upload_file(
                                                file_path + file_name,              # /tmp/hello.txt
                                                S3_BUCKET_PATH + '/' + file_name    # s3-bucket-path/hello.txt      
                                                )

# Use case when you need to upload a PDF file to S3
result = s3.Bucket(S3_BUCKET_NAME).upload_file(
                                                file_path + file_name,              
                                                S3_BUCKET_PATH + '/' + file_name,
                                                ExtraArgs={'ContentEncoding': 'base64',
                                                            'ContentType':'application/pdf'}
                                                )

print(f'File {file_name} uploaded to s3')