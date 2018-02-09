from django.shortcuts import render
from .models import *

# Create your views here.

# 列出书名，并超链接到章节目录
def index(request):
    lunbo = Lunbo.objects.all()
    classify = Classification.objects.all()
    classify1 = Classification.objects.get(id=1)
    classify2 = Classification.objects.get(id=2)
    classify3 = Classification.objects.get(id=3)
    classify4 = Classification.objects.get(id=4)
    classify5 = Classification.objects.get(id=5)
    classify6 = Classification.objects.get(id=6)
    classify7 = Classification.objects.get(id=7)
    book1 = BookName.objects.filter(cfname=1)[0:5]
    book2 = BookName.objects.filter(cfname=2)[0:5]
    book3 = BookName.objects.filter(cfname=3)[0:5]
    book4 = BookName.objects.filter(cfname_id=4)[0:5]
    book5 = BookName.objects.filter(cfname_id=5)[0:5]
    book6 = BookName.objects.filter(cfname_id=6)[0:5]
    book7 = BookName.objects.filter(cfname_id=7)[0:5]

    return render(request, 'index.html',
                  {'book': book, 'lunbo': lunbo, 'classify': classify, 'classify1': classify1, 'title': '首页',
                   'classify2': classify2, 'classify3': classify3, 'classify4': classify4, 'classify5': classify5,
                   'classify6': classify6, 'classify7': classify7, 'book1': book1, 'book2': book2, 'book3': book3,
                   'book4': book4, 'book5': book5, 'book6': book6, 'book7': book7})


# 列出章节目录
def book(request, book_id):
    classify = Classification.objects.all()
    bid = book_id
    name = BookName.objects.get(id=bid)
    chapter = Chapter.objects.filter(cbook=bid)
    count=chapter.count()
    return render(request, 'book.html', {'classify':classify ,'book_name': name, 'chapter': chapter,'count':count,})


def chapter(request, chapter_id):
    classify = Classification.objects.all()
    cid = chapter_id
    chapter = Chapter.objects.get(id=cid)
    content = chapter.ccontent
    # 访问量
    chapter.views = chapter.views + 1
    chapter.save()

    return render(request, 'content.html', {'classify':classify ,'chapter': chapter, 'content': content,'cid':cid})

