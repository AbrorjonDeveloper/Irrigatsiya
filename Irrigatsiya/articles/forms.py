from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    # name = forms.CharField(max_length=200)
    article = forms.FileField()
    # link = forms.URLField(label="Agar maqola Internet saytlarda mavjud bo'lsa ,havola kiriting: ")

    class Meta:
        model = Articles
        fields = ['name', 'file', 'link']
