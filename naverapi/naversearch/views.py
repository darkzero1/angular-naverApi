from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def naverBookSearchApi(request):
	#해당 id secretkey는 git에 넣지않음
	client_id = "sqj46vL3xz4UmCdh5cn3"
	client_secret = "uG9d8QswBN"
	encText = urllib.parse.quote("검색할 단어")
	url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
	# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode==200):
	    response_body = response.read()
	    print(response_body.decode('utf-8'))
	else:
	    print("Error Code:" + rescode)
