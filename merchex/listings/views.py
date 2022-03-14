
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def listings(request):
    lst = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': lst})

def contact(request):
    return render(request, 'listings/contact.html')
    #return HttpResponse("<h1>Nous contacter</h1> <p>La forme saisir des informations</p>")

def about(request):
    return render(request, 'listings/about.html')
    #return HttpResponse("<h1>A propos de nous, c'est à nous</h1> <p>Nous adorons merch !</p>")