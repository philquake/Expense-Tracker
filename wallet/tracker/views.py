from django.template import loader
from django.http import HttpResponse
# Create your views here.

def tracker(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
