from django import forms

from app.models import Recipe, Comment


class RecipeForm(forms.ModelForm):       #create and edit view
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }


class CommentForm(forms.Form):                 # recipe detail
    comment = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control rounded-2'}
                              ))

    class Meta:
        model = Comment
        fields = ('comment',)


class RecipeFormReadOnly(forms.ModelForm):     #delete view

    title = forms.CharField(disabled=True)
    image_url = forms.URLField(disabled=True)
    description = forms.CharField(disabled=True)
    method = forms.CharField(disabled=True)
    ingredients = forms.CharField(disabled=True)
    time = forms.IntegerField(disabled=True)

    class Meta:
        model = Recipe
        exclude = ('user', )
 #       fields = '__all__'


