from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from datetime import datetime

#- "article" or "news";

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        Post.post_rating = Post.post_rating * 3
        self.save()
#         суммарный рейтинг каждой статьи автора умножается на 3;
# суммарный рейтинг всех комментариев автора;
# суммарный рейтинг всех комментариев к статьям автора.
    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, through='SubscribersCategory', related_name='categories' )

    def __str__(self):
        return self.name


class SubscribersCategory(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)



class Post(models.Model):
    POST_TYPE = [("article", "статья"), ("news", "новость")]
    post_type = models.CharField(max_length=10, choices=POST_TYPE)
    post_pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ManyToManyField(Category, through="PostCategory")
    post_headline = models.CharField(max_length=100)
    post_text = models.CharField(max_length=250)
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        # preview_text = Truncator(self.post_text).chars(75)
        preview_text = self.post_text[:75] + (self.post_text[75:] and '..')
        return preview_text


class PostCategory(models.Model):
    post = models.ForeignKey('Category', on_delete=models.CASCADE)
    category = models.ForeignKey('Post', on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=250)
    comment_pub_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

