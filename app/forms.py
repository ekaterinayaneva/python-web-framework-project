from django import forms

from app.models import Recipe, Rating


class RecipeForm(forms.ModelForm):       #create and edit view
    class Meta:
        model = Recipe
        fields = '__all__'


class CommentForm(forms.Form):                 # recipe detail
    comment = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control rounded-2'}
                              ))

    class Meta:
        model = Rating
        fields = ('comment',)


class RecipeFormReadOnly(forms.ModelForm):     #delete view

    title = forms.CharField(disabled=True)
    image_url = forms.URLField(disabled=True)
    description = forms.CharField(disabled=True)
    ingredients = forms.CharField(disabled=True)
    time = forms.IntegerField(disabled=True)
                                  # widget=forms.Textarea(
                                  #     attrs={'class': 'form-control rounded-2'}
                                  # ))
    class Meta:
        model = Recipe
        fields = '__all__'


