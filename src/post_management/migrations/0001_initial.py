# Generated by Django 3.2 on 2024-03-30 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='(未命名)', help_text='The title of the post', max_length=200)),
                ('description', models.TextField(default='', help_text='The description of the post')),
                ('category', models.CharField(default='未分類', help_text='The category of the post', max_length=50)),
                ('main_image', models.CharField(blank=True, help_text='The source URL of banner image of the post', max_length=2000, null=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('intro_title', models.CharField(default='', help_text='The title of the introduction', max_length=200)),
                ('intro_content', models.TextField(default='', help_text='The HTML content of the introduction')),
                ('modify_user', models.ForeignKey(help_text='The user that modify this post', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PM_Post',
                'ordering': ['-publish_date', 'id'],
            },
        ),
        migrations.CreateModel(
            name='RankItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sort_index', models.IntegerField(default=0, help_text='The order of the item in the rank list')),
                ('title', models.CharField(default='', help_text='The title of the item', max_length=200)),
                ('content', models.TextField(default='', help_text='The HTML content of the item')),
                ('post', models.ForeignKey(help_text='The post that the item belongs to', on_delete=django.db.models.deletion.CASCADE, to='post_management.post')),
            ],
            options={
                'db_table': 'PM_RankItem',
                'ordering': ['post', 'sort_index'],
            },
        ),
    ]
