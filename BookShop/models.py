from django.db import models


# Create your models here.
class Classification(models.Model):
    class Meta:
        db_table = 'classification'

    cname = models.CharField(max_length=18)

    def __str__(self):
        return self.cname


class BookName(models.Model):
    class Meta:
        db_table = 'bookname'

    bname = models.CharField(max_length=30)
    bintroduction = models.CharField(max_length=3000)
    bcomment = models.TextField(default=None)
    cfname = models.ForeignKey(Classification, on_delete=models.CASCADE)


class Chapter(models.Model):
    class Meta:
        db_table = 'chapter'
    clist=models.CharField(max_length=30)
    ccontent=models.TextField()
    cbook=models.ForeignKey(BookName, on_delete=models.CASCADE)
