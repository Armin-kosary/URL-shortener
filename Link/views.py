from django.shortcuts import render
from .models import Link
from django.shortcuts import redirect
# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, "Link/index.html")
    
    if request.method == "POST":
        url = request.POST["url"]
        new_link = Link(
            link_address = url,
        )
        new_link.save()
        return render(request, "Link/index.html", {"link" : new_link.short_link})
    
def redirect_link(request, ShortLink):
    get_main_link = Link.objects.filter(short_link = ShortLink).first()
    return redirect(get_main_link.link_address)
