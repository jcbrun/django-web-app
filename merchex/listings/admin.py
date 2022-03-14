from django.contrib import admin

from listings.models import Band

from listings.models import Listing

#admin.site.register(Band)

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'id', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'band', 'type')

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Listing, ListingAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument