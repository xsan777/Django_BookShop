from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


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
                   'book4': book4, 'book5': book5, 'book6': book6, 'book7': book7, })


# 显示该类图书
def classify(request, classify_id, page_id):
    classify = Classification.objects.all()
    classify1 = classify_id
    books = BookName.objects.filter(cfname=classify1)
    # 分页显示该类图书
    paginator = Paginator(books, 10)
    page = paginator.page(page_id)
    classify_name = Classification.objects.get(id=classify_id)
    # 创建翻页链接
    pagenum = int(page_id)
    page_next = pagenum + 1
    page_last = pagenum - 1
    if page_last == 0:
        page_last = 1
    if page_next > paginator.num_pages:
        page_next = paginator.num_pages
    return render(request, 'classify.html',
                  {'books': page, 'classify_name': classify_name, 'classify': classify, 'page_next': page_next,
                   'page_last': page_last})


# 列出章节目录
def book(request, book_id):
    classify = Classification.objects.all()
    bid = book_id
    name = BookName.objects.get(id=bid)
    chapter = Chapter.objects.filter(cbook=bid)
    count = chapter.count()
    return render(request, 'book.html',
                  {'classify': classify, 'book_name': name, 'chapter': chapter, 'count': count, 'bid': bid})


# 列出本章内容
def chapter(request, chapter_id, book_id):
    classify = Classification.objects.all()
    cid = chapter_id
    cidi = int(cid)
    bid = book_id
    chapter_content = Chapter.objects.filter(cbook=bid).count()
    chapter = Chapter.objects.get(id=cid)
    # 创建下一章链接
    zuihou = ''
    cid1 = cidi + 1
    cid2 = cidi - 1
    if cid2 == 0:
        cid2 = 1
    if cidi == chapter_content:
        cid1 = chapter_content
        zuihou = '本书以读完，谢谢品读'
    next_c = str(cid1)
    last_c = str(cid2)
    content = chapter.ccontent
    # 访问量
    chapter.views = chapter.views + 1
    chapter.save()

    return render(request, 'content.html',
                  {'classify': classify, 'chapter': chapter, 'content': content, 'cid': cid, 'blink': book_id,
                   'next_c': next_c, 'last_c': last_c, 'zui': zuihou})
