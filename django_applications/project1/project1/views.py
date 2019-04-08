from django.http import HttpResponse


def index(request):
    page = """<a href="/app1/">app1</a>
    <a href="/app2/">app2</a>"""
    return HttpResponse(page)