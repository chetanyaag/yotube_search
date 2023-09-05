import boto3

# Set up AWS credentials and region
s3 = boto3.client('s3', aws_access_key_id='AKIARG3UQKCMZAXUXG76', aws_secret_access_key='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', region_name='us-west-1')

# Upload the image to a specific bucket
bucket_name = 'instagram-video'
file_path = r'videos/Krishna Makhan Chor Song Cover  THE 9TEEN shorts.mp4'
s3.upload_file(file_path, bucket_name, 'image2.mp4')

# bucket_url = f"https://{bucket_name}.s3.amazonaws.com/"
# image_url = f"{bucket_url}image.jpg"
