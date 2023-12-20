import boto3
import io
import base64

session = boto3.Session(
    aws_access_key_id="AKIATV7T4KLWHI2ELWWZ",
    aws_secret_access_key="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",
    region_name="us-west-2"
)
client = session.client('rekognition')


class FaceLivenessError(Exception):
    '''
    Represents an error due to Face Liveness Issue.
    '''
    pass


def do_liveness_check(session_id):

    '''
    Get Session result.
    '''
    try:
        response = client.get_face_liveness_session_results(SessionId=session_id)
        resp = format(response)
        confidence = response.get("Confidence")
        isLive = confidence is not None and float(confidence) > 10
        status = response.get("Status")
        imgByte = response.get("ReferenceImage")
        imageStream = io.BytesIO(imgByte.get("Bytes"))
        referenceImage = base64.b64encode(imageStream.getvalue())

        print('Confidence: ' + "{:.2f}".format(confidence) + "%")
        print('Status: ' + status)

        return {"response": resp, "status": status, "confidence": confidence, "isLive": isLive, "img": referenceImage}

    except client.exceptions.AccessDeniedException:
        raise FaceLivenessError("Access Denied")

    except client.exceptions.InternalServerError:
        raise FaceLivenessError("Internal Server Error")

    except client.exceptions.InvalidParameterException:
        raise FaceLivenessError('InvalidParameterException')

    except client.exceptions.SessionNotFoundException:
        raise FaceLivenessError('SessionNotFound')

    except client.exceptions.ThrottlingException:
        raise FaceLivenessError('ThrottlingException')

    except client.exceptions.ProvisionedThroughputExceededException:
        raise FaceLivenessError('ProvisionedThroughputExceededException')
