from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    class Meta:
        db_table = "PM_Post"
        ordering = ['-publish_date', 'id']

    def __str__(self):
        return f"[{id}] {self.title}"

    id = models.AutoField(
        primary_key=True,
    )
    title = models.CharField(
        default="(未命名)",
        max_length=200,
        help_text="The title of the post",
    )
    description = models.TextField(
        default="",
        help_text="The description of the post",
    )
    category = models.CharField(
        default="未分類",
        max_length=50,
        help_text="The category of the post",
    )
    main_image = models.CharField(
        blank=True,
        null=True,
        max_length=2000,
        help_text="The source URL of banner image of the post",
    )

    publish_date = models.DateTimeField(
        auto_now_add=True
    )
    last_modify = models.DateTimeField(
        auto_now=True
    )
    modify_user = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.CASCADE,
        help_text="The user that modify this post",
    )

    intro_title = models.CharField(
        default="",
        max_length=200,
        help_text="The title of the introduction",
    )
    intro_content = models.TextField(
        default="",
        help_text="The HTML content of the introduction",
    )

    
class RankItem(models.Model):
    class Meta:
        db_table = "PM_RankItem"
        ordering = ['post', 'sort_index']
    def __str__(self) -> str:
        return super().__str__()
    
    id = models.AutoField(
        primary_key=True,
    )
    sort_index = models.IntegerField(
        default=0,
        help_text="The order of the item in the rank list",
    )
    title = models.CharField(
        default="",
        max_length=200,
        help_text="The title of the item",
    )
    content = models.TextField(
        default="",
        help_text="The HTML content of the item",
    )


    post = models.ForeignKey(
        Post,
        blank=False,
        on_delete=models.CASCADE,
        help_text="The post that the item belongs to",
    )