# import mimetypes
import os

# import boto3
# from botocore.config import Config


def run():
    # Github converts actions inputs into env variables which can be accessed here
    # INPUT_<Action Input name>
    bucket = os.environ['INPUT_BUCKET']
    bucket_region = os.environ['INPUT_BUCKET-REGION']
    dist_folder = os.environ['INPUT_DIST-FOLDER']

    print(f'bucket: {bucket}')
    print(f'bucket_region: {bucket_region}')
    print(f'dist_folder: {dist_folder}')

    # configuration = Config(region_name=bucket_region)

    # s3_client = boto3.client('s3', config=configuration)

    # for root, subdirs, files in os.walk(dist_folder):
    #     for file in files:
    #         s3_client.upload_file(
    #             os.path.join(root, file),
    #             bucket,
    #             os.path.join(root, file).replace(dist_folder + '/', ''),
    #             ExtraArgs={"ContentType": mimetypes.guess_type(file)[0]}
    #         )

    print('Upload to S3 complete!')

    website_url = f'http://{bucket}.s3-website-{bucket_region}.amazonaws.com'

    # The below code sets the 'website-url' output (the old ::set-output syntax isn't supported anymore - that's the only thing that changed though)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'website-url={website_url}', file=gh_output)


if __name__ == '__main__':
    run()
