from django.forms import ModelForm

from tweets.models import Tweet
__author__ = 'nealshultz'


class TweetForm(ModelForm):
    class Meta:
        model = Tweet