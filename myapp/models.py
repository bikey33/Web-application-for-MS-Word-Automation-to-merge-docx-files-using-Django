from django.db import models
class Mydocument(models.Model):
    file1 = models.FileField(upload_to='documents/word/')
    file2 = models.FileField(upload_to='documents/word/')
    file3 = models.FileField(upload_to='documents/word/')
    file_processed = models.FileField(upload_to='',null=True,default='documents/word/ssm.docx')

# Create your models here.
