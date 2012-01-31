from django.template import loader, Context
from django.http import HttpResponse

def playlists(request):
    t = loader.get_template("playlists.html")
    c = Context({})
    return HttpResponse(t.render(c))