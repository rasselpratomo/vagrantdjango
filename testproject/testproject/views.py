from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def greetings(request):
    template = get_template('greetings.html')
    html = template.render({'name': 'world'})
    return HttpResponse(html)
