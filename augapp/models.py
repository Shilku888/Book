from django.db import models

# Create your models here.
class Books(models.Model):
    name= models.CharField(max_length=100,blank=False,null=False)
    price= models.IntegerField(blank=False,null=False)

    def __str__(self):
        return  self.name

class Author(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    bookname = models.ForeignKey(Books,on_delete=models.CASCADE,null=True,blank=True, related_name='bookname')

    def __str__(self):
        return self.name
