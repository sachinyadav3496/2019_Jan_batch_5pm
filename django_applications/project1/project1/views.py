from django.http import HttpResponse


def index(request):
    page = """
    <!Doctype html>
    <html>
    <head> <title>HOME</title></head>
    <body><div>
    <a href="/app1/">app1</a>
    <a href="/app2/">app2</a>
    </div>
    </body>
    </html>
    """
    return HttpResponse(page)