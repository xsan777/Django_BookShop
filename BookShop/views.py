from django.shortcuts import render
from .models import *


# Create your views here.

# 列出书名，并超链接到章节目录
def index(request):
    book = BookName.objects.all()

    return render(request, 'index.html', {'book': book})


# 列出章节目录
def book(request, book_id):
    bid = book_id
    name = BookName.objects.get(id=bid)
    cname = name.bname  # 取出书名
    chapter = Chapter.objects.filter(pk=bid)

    return render(request, 'book.html', {'book_name': cname, 'chapter': chapter})


def chapter(request, chapter_id):
    cid = chapter_id
    chapter = Chapter.objects.get(id=cid)
    content = chapter.ccontent
    # 访问量
    chapter.views = chapter.views + 1
    chapter.save()

    return render(request, 'content.html', {'chapter': chapter, 'content': content})
