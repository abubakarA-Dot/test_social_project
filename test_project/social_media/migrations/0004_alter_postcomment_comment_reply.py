# Generated by Django 4.1.3 on 2022-11-26 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0003_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='comment_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_media.postcomment'),
        ),
    ]
