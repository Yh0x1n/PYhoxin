from django.shortcuts import render, get_object_or_404
from .models import AuthorDB, FraseDB

# Create your views here.
def indexView(request):

    autor = AuthorDB.objects.all().order_by('id')

    return render(request, 'index.html', {'autor' : autor})

def autorView(request, id):

    autor = get_object_or_404(AuthorDB, id = id)
    return render(request, 'autor.html', {'autor' : autor})