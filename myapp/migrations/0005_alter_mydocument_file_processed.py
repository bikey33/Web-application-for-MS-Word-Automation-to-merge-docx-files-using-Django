# Generated by Django 4.0.6 on 2022-07-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_document_mydocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydocument',
            name='file_processed',
            field=models.FileField(default='documents/word/ssm.docx', null=True, upload_to='documents/word/'),
        ),
    ]