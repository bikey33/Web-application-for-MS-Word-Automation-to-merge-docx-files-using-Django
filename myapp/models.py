from django.db import models
from django.utils import timezone
from django.urls import reverse

class Mydocument(models.Model):
    file1 = models.FileField(upload_to='documents/word/')
    file2 = models.FileField(upload_to='documents/word/')
    file3 = models.FileField(upload_to='documents/word/')
    file_processed = models.FileField(upload_to='',null=True,default='documents/word/ssm.docx')

# Create your models here.
class Bugreports(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 50)
    report = models.TextField(max_length =1500)
    report_date= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')