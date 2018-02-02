from django.db import models


# Create your models here.
class Classification(models.Model):
    class Meta:
        db_table = 'classification'

    cname = models.CharField(r'分类名', max_length=18, db_column="分类名")

    def __str__(self):
        return self.cname


class Size(models.Model):
    class Meta:
        db_table = 'size'

    size = models.CharField(r'字数分类', max_length=18, db_column="字数分类")

    def __str__(self):
        return self.size


class BookName(models.Model):
    class Meta:
        db_table = 'bookname'

    bname = models.CharField(r'书名', max_length=30, db_column="书名", db_index=True)
    bintroduction = models.CharField(r'简介', max_length=3000, db_column="简介")
    bcomment = models.TextField(r'评论', null=True, blank=True, db_column="评论")
    bauthor = models.CharField(r'作者', max_length=18, db_column="作者", db_index=True)
    bsize = models.IntegerField(r'字数', db_column="字数")
    img = models.ImageField(upload_to='static/bookshop/img')
    bfsize = models.ForeignKey(Size, on_delete=models.CASCADE, db_column="分类字数")
    cfname = models.ForeignKey(Classification, on_delete=models.CASCADE, db_column="类名")

    def __str__(self):
        return self.bname


class Chapter(models.Model):
    class Meta:
        db_table = 'chapter'

    clist = models.CharField(r'目录', max_length=30, db_index=True, )
    ccontent = models.TextField(r'内容')
    creattime = models.DateField(r'创建时间', auto_now_add=True, db_index=True)
    cbook = models.ForeignKey(BookName, on_delete=models.CASCADE)
    views = models.IntegerField(r'点击数', default=0)

    def __str__(self):
        return self.clist


class Lunbo(models.Model):
    class Meta:
        db_table = 'lunbo'

    img = models.ImageField(r'轮播图片',upload_to='static/bookshop/img/lunbo')

    def __str__(self):
        return self.img
