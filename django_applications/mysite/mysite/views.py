from django.http import HttpResponse

def index(request):
    page = """<a href="/">Home</a>
              <a href="/data/">Data</a>
              <a href="/app1/">App1</a>
              <h1>Welcome To Home</h1>"""
    return HttpResponse(page)


def data(request):
    page = """<a href="/">Home</a>
              <a href="/data/">Data</a>
              <a href="/app1/">App1</a>
              <h1>You are at Data Page</h1>"""
    return HttpResponse(page)