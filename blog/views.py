from django.http import HttpResponse

from .models import Post
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def posts(request):
    latest_post_list = Post.objects.order_by("-published_at")
    output = ",<br />".join([q.title for q in latest_post_list])
    return HttpResponse(output)

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)


def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)


def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)

def test(request, post_id):
    return HttpResponse("This is a test")