from __future__ import absolute_import

from celery import shared_task, chain
from rq.decorators import job

from ribao.models import *
from worker import conn
import urllib2
import re

#-------methods of articles----------
@job('default', connection=conn, timeout=5)
def article_url(url):
    html = urllib2.urlopen(url).read()
    m = re.search(r'<title>(.*)</title>', html, flags=re.I)
    title = m and m.group(1) or ''
    print title
    return article_add.delay(title,url)

@job('default', connection=conn, timeout=5)
def article_add(title_add,url_add):
    a=Article.objects.create(title=title_add,raw_url=url_add)
    return 'No.%d Article is now added as %s' % (a.pk, a.title)

@job
def article_comment(article_index,comment_add):
    a=Article.objects.get(pk=article_index)
    a.comment=comment_add
    a.save()
    d = Daily.objects.all()
    for daily in d:
        num=daily.pk
    article_publish.apply_async((a.pk,num),countdown=3)
    return 'Comment No.%d complete'% a.pk+'     '+str(num)

@job
def article_categorize(article_index,category_name):
    #if category_check(category_index):
        c=Category.objects.filter(name=category_name)
        a=Article.objects.get(pk=article_index)
        a.category=c
        a.save()
        return 'Article No.%d\'s category has been changed to %s' % (a.pk, c.pk)
    #return 'error, category does not exist'

@job
def article_publish(article_index,daily_index):
    a=Article.objects.get(pk=article_index)
    d=Daily.objects.get(pk=daily_index)
    #if daily_check_full(d.pk)
    a.daily=d
    a.save()
    daily_check_full.apply_async((d.pk,),countdown=2)
    return "Article %d %s has been published to daily %d successfully" % (a.pk, a.title, d.pk)

@job
def article_delete(article_index):
    a=Article.objects.get(pk=article_index)
    a.delete()
    return 'article %d has been deleted' % a.pk

#----------methods of daily-------------

@job
def daily_add():
    return Daily.objects.create()

@job
def daily_publish(daily_index):
    pass
    print 'aaaaaaaaaaaaaaaaaa%d' % daily_index
    #do sth

@job
def daily_check_full(daily_index):
    d=Daily.objects.get(pk=daily_index)
    article_list=Article.objects.filter(daily=d)
    if len(article_list)==5:
        daily_publish.apply_async((d.pk,),countdown=3)
        return True
    return False


@job
def list(daily_index):
    result = daily_check_full(daily_index)
    article_list = 'ERROR'
    if result == True:
        d=Daily.objects.get(pk=daily_index)
        article_list = Article.objects.filter(daily=d)
    return article_list

#------------methods of category---------
@job
def category_add(category_name):
    c=Category.objects.create(name=category_name)
    return c

def category_delete(category_name):
    article_list=category_list_article(category_name)
    for article in article_list:
        article.category=null
        article.save()
    c=Category.objects.get(name=category_name)
    c.delete()
    return c

def category_list_article(category_name):
    c=Category.objects.get(name=category_name)
    return Article.objects.filter(category=c)

@job
def check(daily_index):
    result = True
    try:
        d=Daily.objects.get(pk=int(daily_index))
    except:
        result=False
        #Daily.objects.create()
        #check.apply_async((daily_index + 1,), countdown=3)
        return "%d NO DAILY" % daily_index
    article_list = Article.objects.filter(daily = d)
    try:
        p=article_list[4].title
    except:
        #check.apply_async((daily_index,), countdown=3)
        return "%d NOT FULL" % daily_index
    flag = daily_index
    for article in article_list:
        if article.status=="0":
            #check.apply_async((daily_index,), countdown=3)
            return "%d NOT READY" % daily_index
    chain = publish_daily.s(daily_index)|check.s()
    chain()
    return "SENDING"

@job
def add_to_daily(article_index,daily_index):
    try:
        article = Article.objects.get(pk=article_index)
    except:
        return "ERROR: ARTICLE DOES NOT EXSIT"
    try:
        article.daily = Daily.objects.get(pk=daily_index)
    except:
        Daily.objects.create()
        daily_index = daily_index + 1
        add_to_daily.apply_async((article,daily_index),countdown=3)
    article.save()
    return 'article %d %s has been added to daily %d successfully.' % (article.pk, article.title, daily_index)

@job
def publish_daily(daily_index):
    if email_daily.apply_async((daily_index,), countdown=3):
        d = Daily.objects.get(pk=daily_index)
        d.status="2"
        d.save()
        return daily_index+1
    return daily_index


@job
def email_daily(daily_index):
    return True

@job
def add(x, y):
    return x + y


@job
def mul(x, y):
    return x * y


@job
def xsum(numbers):
    return sum(numbers)
