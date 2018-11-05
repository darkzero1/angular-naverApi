from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponseRedirect, Http404,JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

# Create your views here.
@csrf_protect
def naverBookSearchApi(request):

	#해당 id secretkey는 git에 넣지않음
	client_id = getattr(settings, 'CLIENT_ID')
	client_secret = getattr(settings, 'CLIENT_SECRET')
	encText = urllib.parse.quote(request.POST['search_name'])
	url = "https://openapi.naver.com/v1/search/book.json?query="+encText+"&display=10&start=1"
	# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode==200):
		response_body = response.read().decode("utf-8")
		jsondata = json.loads(response_body)
		return JsonResponse(jsondata, safe=False)
	else:
		print("Error Code:" + rescode)

def naverBookTemplate(request):
	return render(request, "naversearch/template.html",None)
