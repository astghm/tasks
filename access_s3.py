import boto3
import argparse

def main():

    ACCESS_KEY_ID = 'AKIAUTJ2H5B6J55J4GFI'
    ACCESS_SECRET_KEY = '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'

    s3 = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=ACCESS_SECRET_KEY)

    parser = argparse.ArgumentParser(description='Loading the file to s3 bucket')
    parser.add_argument('-b','--bucket_name', type=str)
    parser.add_argument('-f','--file_name', type=str)
    args = parser.parse_args()

    s3.upload_file(args.file_name, args.bucket_name, args.file_name)

    upload_s3(args.bucket_name, args.file_name)

if __name__ == '__main__':
    main()

