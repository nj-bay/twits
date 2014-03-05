from django.shortcuts import render, redirect
from tweets.forms import TweetForm

from tweets.models import Tweet
# Create your views here.
def home(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/")
    else:
        form = TweetForm()
        data = {'form': form}
        return render(request, "home.html", data)


def tweets(request):
    tweets = Tweet.objects.all()
    data = {'tweets': tweets}
    return render(request, "tweets.html", {'tweets': tweets})
