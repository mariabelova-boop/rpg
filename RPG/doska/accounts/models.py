from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    TANKS = 'TN'
    HILL = 'HL'
    DD = 'DD'
    MERCHANTS = 'MR'
    GUILD_MASTER = 'GM'
    QUEST_GIVERS = 'QG'
    BLACKSMITHS = 'BS'
    POTION_MAKERS = 'PM'
    MASTERS_OF_KNOWLEDGE = 'MK'
    TANNERS = 'TR'

    CATEGORY_CHOISE = (
        (TANKS, "ТАНКИ"),
        (HILL, "ХИЛЫ"),
        (DD, "ДД"),
        (MERCHANTS, "ТОРГОВЦЫ"),
        (GUILD_MASTER, "ГИЛДМАТЕРА"),
        (QUEST_GIVERS, "КВЕСТГИВЕРЫ"),
        (BLACKSMITHS, "КУЗНЕЦЫ"),
        (POTION_MAKERS, "ЗЕЛЬЕВАРЫ"),
        (MASTERS_OF_KNOWLEDGE, "МАСТЕРА ЗАКЛИНАНИЙ"),
        (TANNERS, "КОЖЕВНИКИ"),
    )

    small_string = models.CharField(max_length=64, default="Default value")
    big_string = models.TextField()
    data_post = models.DateField(auto_now_add = True)
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOISE, default="ВЫБЕРИТЕ КАТЕГОРИЮ ОБЪЯВЛЕНИЯ")
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    #posts = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.big_string.title()


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.title()


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.title()

class Subscription(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='subscriptions')
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE, related_name='subscriptions')