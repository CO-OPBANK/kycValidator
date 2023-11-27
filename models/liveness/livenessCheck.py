import boto3

session = boto3.Session(
    aws_access_key_id="AKIATV7T4KLWHI2ELWWZ",
    aws_secret_access_key="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",
    region_name="us-west-2"
)
client = session.client('rekognition')


def do_liveness_check(session_id):
    response = client.get_face_liveness_session_results(SessionId=session_id)

    confidence = response.get("Confidence")
    status = response.get("Status")

    print('Confidence: ' + "{:.2f}".format(confidence) + "%")
    print('Status: ' + status)

    return {"status": status, "response": response}
