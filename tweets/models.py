from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Abstract base class for self updating """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class User(TimeStampedModel):
    name = models.CharField(max_length=255)


    def __unicode__(self):
        return self.name


class Tweet(TimeStampedModel):
    tweet = models.CharField(max_length=140)
    user = models.ForeignKey(User)



class Comment(TimeStampedModel):
    comment = models.CharField(max_length=255)


class Likes(models.Model):
    like = models.SmallIntegerField()