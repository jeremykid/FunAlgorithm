import requests
import json
import time
import base64

def faceppAPI(filepath):
    facepp_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    api_key = 'Bn7swhGpvtzxS9uMWG-0CkacJY-_gt-4'
    api_secret = 'tNCF8Wd-xjtw-qyQn47yjZh8RzLkVBkU'

    try:
        params = dict(api_key=api_key, api_secret=api_secret, image_url=filepath, return_landmark=0,
                      return_attributes="gender,age,smiling,glass")
        result = requests.post(url=facepp_url, params=params, timeout=15)
        return result.text
    except Exception as e:
        print(e)
        return None

def faceppAPIFile(filepath):
    facepp_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    api_key = 'Bn7swhGpvtzxS9uMWG-0CkacJY-_gt-4'
    api_secret = 'tNCF8Wd-xjtw-qyQn47yjZh8RzLkVBkU'

    try:
        fr=open(filepath,'rb')
        params = dict(api_key=api_key, api_secret=api_secret, image_file=fr, return_landmark=0,
                      return_attributes="gender,age,smiling,glass")
        result = requests.post(url=facepp_url, params=params, timeout=15, headers = {'Content-Type':  'application/json'})
        return result.text
    except Exception as e:
        print(e)
        return None

def main():
    #print faceppAPI("https://github.com/jeremykid/FunAlgorithm/blob/master/faceRegonization/sample.jpg?raw=true")
    print faceppAPIFile("sample.jpg")
main()