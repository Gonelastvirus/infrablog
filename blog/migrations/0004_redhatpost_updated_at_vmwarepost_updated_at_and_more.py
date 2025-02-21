# Generated by Django 5.1.6 on 2025-02-20 15:00

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_vmwarepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='redhatpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vmwarepost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='redhatpost',
            name='author',
            field=models.CharField(default='Admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='redhatpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='vmwarepost',
            name='author',
            field=models.CharField(default='Admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='vmwarepost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
