
from django.http import HttpResponse
from django.shortcuts import render

# Ajouter ici la reference à un model dès que l'on crée une nouvelle model
from listings.models import Band, Listing

# Ajouter ici la reference à une form dès que l'on crée une nouvelle form
from listings.forms import ContactUsForm, BandForm, ListingsForm


from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit
    
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def listings_list(request):
    lst = Listing.objects.all()
    return render(request, 'listings/listings_list.html', {'listings': lst})

def listings_detail(request, id):
    lst = Listing.objects.get(id=id)
    return render(request, 
            'listings/listings_detail.html',
            {'lst': lst})


def listings_create(request):
    if request.method == 'POST':
        form = ListingsForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            lst = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listings-detail', lst.id)
    else:
        form = ListingsForm()
    return render(request,
            'listings/listings_create.html',
            {'form': form})


def listings_update(request, id):
    lst = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingsForm(request.POST, instance=lst)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listings-detail', lst.id)
    else:
        form = ListingsForm(instance=lst)

    return render(request,
                'listings/listings_update.html',
                {'form': form})

def listings_delete(request, id):
    lst = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        lst.delete()
        # rediriger vers la liste des groupes
        return redirect('listings-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/listings_delete.html',
                    {'listings': lst})

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')  # ajoutez cette instruction de retour
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
            'listings/contact.html',
            {'form': form}) 

def email_sent(request):
    return render(request, 'listings/email_sent.html')


def about(request):
    return render(request, 'listings/about.html')
    #return HttpResponse("<h1>A propos de nous, c'est à nous</h1> <p>Nous adorons merch !</p>")