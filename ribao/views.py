from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from ribao.models import *
from ribao.serializers import *
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, renderers, viewsets
from ribao.permissions import *
#from ribao.tasks import *
from rq import Queue
from worker import conn
q=Queue('low', connection=conn)
from ribao.utils import *
from weibo import APIClient

APP_KEY = '2318693502' # app key
APP_SECRET = '43db4ea1a6d277b9e65249f9ab8e11d2' # app secret
CALLBACK_URL = 'http://healthdaily.applinzi.com/callback' # callback url
ACCESS_TOKEN=''


# Create your views here.
def callback(request):
    code = request.REQUEST.get('code').encode('utf-8')
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri= 'http://healthdaily.applinzi.com/callback')
    r = client.request_access_token(code,'http://healthdaily.applinzi.com/callback')
    ACCESS_TOKEN = r.access_token #
    expires_in = r.expires_in #
    client.set_access_token(ACCESS_TOKEN, expires_in)
    client.statuses.update.post(status=u'aaaaa',visible=1)
    ACCESS_TOKEN=client.access_token
    return HttpResponse('%s' % ACCESS_TOKEN)

def sina(request):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    YOUR_CLIENT_ID='2318693502'
    YOUR_REGISTERED_REDIRECT_URI='http://healthdaily.applinzi.com/callback'
    return render_to_response('sina.html',{'url':url,'YOUR_CLIENT_ID':YOUR_CLIENT_ID,'YOUR_REGISTERED_REDIRECT_URI':YOUR_REGISTERED_REDIRECT_URI})

def adda(request):
    return render_to_response('adda.html')

def addarticle(request):
    url = request.GET['a']
    q = Queue('low', connection=conn)
    q.enqueue(article_add, '123', url)
    article_add.delay('abc',url)
    return HttpResponse(url)

def sb(request):
    return render_to_response('123123.html')

def homepage(request):
    return render_to_response('index.html')


def article(request,num='1'):
    a = Article.objects.get(id=num)
    return render_to_response('daily.html',{'a':a})

def dailyhomepage(request,page='1'):
    CURRENT_URL = request.path
    PREVIOUS_URL = CURRENT_URL.replace(page,str(int(page)-1))
    NEXT_URL = CURRENT_URL.replace(page,str(int(page)+1))
    page = int(page)
    DAILY_LIST=[]
    ARTICLE_LIST=[]
    #for d_num in range(page * 4 - 3, page * 4 + 1):
    #    if not page==1:
    #        index = (d_num) % (page * 4 - 3)
    #    if page==1:
    #        index = d_num - 1
    #    try:
    #        DAILY_LIST.append(Daily.objects.get(id=d_num))
    #        ARTICLE_LIST.append([])
    #    except:
    #        flag=0
    d = Daily.objects.get(id=page)
    ARTICLE_LIST=Article.objects.filter(daily=d)
    for num in range(d.id,d.id+5):
        try:
            DAILY_LIST.append(Daily.objects.get(id=num))
        except:
            break
    return render_to_response('dailyhomepage.html',{ 'PREVIOUS_URL':PREVIOUS_URL, 'NEXT_URL':NEXT_URL, 'page':page, 'DAILY_LIST':DAILY_LIST, 'ARTICLE_LIST':ARTICLE_LIST})
    ARTICLE_LIST[index] = Article.objects.filter(daily=Daily.objects.get(id=d_num))
        #for a_num in ARTICLE_NUM_LIST[index]:
        #    ARTICLE_LIST[index].append(Article.objects.get(id=a_num))

    return render_to_response('dhome.html',{'flag':flag, 'd_num':d_num,'PREVIOUS_URL':PREVIOUS_URL, 'NEXT_URL':NEXT_URL, 'page':page, 'DAILY_LIST':DAILY_LIST, 'ARTICLE_LIST':ARTICLE_LIST})

def daily(request,num='1'):
    d = Daily.objects.get(id=num)
    #ARTICLE_NUM_LIST = [d.article_num1,d.article_num2,d.article_num3,d.article_num4,d.article_num5]
    ARTICLE_LIST = Article.objects.filter(daily=d)
    return render_to_response('projexam.html',{'d':d, 'ARTICLE_LIST':ARTICLE_LIST})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = DailySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
