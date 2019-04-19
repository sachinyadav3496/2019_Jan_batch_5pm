
from django.http import JsonResponse,HttpResponse
from blog.models import Story 
def index(request):
    raw_data = Story.objects.all().order_by("-pub_date")
    data = []
    for post in raw_data : 
        content = { 
            'title':post.title,
            'author':post.author.username,
            'author_email':post.author.email,
            'topic' : post.topic,
            'content':post.content,
        }
        data.append(content)
    print(data)
    return JsonResponse(data,safe=False)