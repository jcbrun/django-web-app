
from django import forms

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


# Ajout de la ligne suivante car on va créer la forme en la déduisant du model
from listings.models import Band
     
class BandForm(forms.ModelForm):
   class Meta:
      model = Band
      # fields = '__all__' # supprimez cette ligne
      exclude = ('active', 'official_homepage')  # ajoutez cette ligne
      
      
      
# Ajout de la ligne suivante car on va créer la forme en la déduisant du model
from listings.models import Listing
     
class ListingsForm(forms.ModelForm):
   class Meta:
      model = Listing
      fields = '__all__' # supprimez cette ligne
      # exclude = ('active', 'official_homepage')  # ajoutez cette ligne