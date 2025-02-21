# Generated by Django 5.1.6 on 2025-02-20 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_text_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='redhat_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.redhatpost'),
        ),
        migrations.AddField(
            model_name='comment',
            name='vmware_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.vmwarepost'),
        ),
    ]
