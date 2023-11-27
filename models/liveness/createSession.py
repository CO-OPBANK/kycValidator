import boto3

session = boto3.Session(
    aws_access_key_id="AKIATV7T4KLWHI2ELWWZ",
    aws_secret_access_key="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",
    region_name="us-west-2"
)
client = session.client('rekognition')


def create_session():
    response = client.create_face_liveness_session()
    session_id = response['SessionId']

    print('SessionId: ' + session_id)

    return session_id
