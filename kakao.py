# pip install requests

import requests
import json

# 이미지가 있는 image_url을 통해 file_name 파일로 저장하는 함수
def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    if img_response.status_code == 200: # 요청에 성공했다면
        with open(file_name,"wb") as fp: # 파일저장
            fp.write(img_response.content)

# kakao developers에서 제공하는 이미지 검색 get url
url = "https://dapi.kakao.com/v2/search/image"
# kakao developers > 내어플리케이션에서 발급받은 REST API키 입력
headers = {"Authorization" : "KakaoAK b37a8210d91a1711f6232a1c721ce3cb"}
data = {"query" : "펭수"}

#이미지 검색 요청
response = requests.post(url, headers=headers, data=data)

if response.status_code != 200: # 요청에 실패했다면
    print("오류: ", response.json())
else: # 요청에 성공했다면
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        count += 1
        file_name = "test_%d.jpg" %(count)
        save_image(image_info['image_url'], file_name)

