import requests
import json
import time
import base64

def main():
    filepath = raw_input("input the url:")
    print (filepath)
    facepp_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    key = 'Bn7swhGpvtzxS9uMWG-0CkacJY-_gt-4'
    secret = 'tNCF8Wd-xjtw-qyQn47yjZh8RzLkVBkU'

    try:
        params = dict(api_key=key, api_secret=secret, image_url=filepath, return_landmark=0,
                      return_attributes="gender,age,smiling,glass")
        print(params)
        # result = requests.post(url=facepp_url, params=params, timeout=15)
        # output = json.loads(result.text)
        # print ("gender :"+output['faces'][0]['attributes']['gender']['value'])
        # print ("age :"+str(output['faces'][0]['attributes']['age']['value']))
    except Exception as e:
        print(e)
main()