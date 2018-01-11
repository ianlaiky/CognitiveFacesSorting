import json
import urllib
import requests

from pprint import pprint
from os.path import expanduser

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'ad93c3e88a8c4cfcbe71a73b4005f779',
}

params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses',
})

url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?%s' % params

img = open(expanduser('./faces/1 (1).jpg'), 'rb')
response = requests.post(url, data=img, headers=headers)
pprint(response.json())
if response.status_code != 200:
    raise ValueError(
        'Request to Azure returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )