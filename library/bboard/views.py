from django.shortcuts import render
from .models import Bb

def index(request):
    bbs = Bb.objects.order_by('-give_in')
    return render(request, 'bboard/index.html', {'bbs': bbs})
