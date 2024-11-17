import boto3

s3 = boto3.resource("s3")
file_name = "D:/python/backups/backup_2024-11-09.tar.gz"
region = "us-west-1"
bucket_name = "bucket-using-python"


def show_bucket(s3):
    for b in s3.buckets.all():
        print(b.name)

def create_bucket(s3,name,region):
    s3.create_bucket(Bucket=name,
        CreateBucketConfiguration={
        'LocationConstraint': region
    },)
    print("Bucket Created using Python")

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name,'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body = data)
    print("Backup uploaded successfully")

show_bucket(s3)
#create_bucket(s3,name,region)
#upload_backup(s3,file_name,bucket_name,"s3-backup2.tar.gz")