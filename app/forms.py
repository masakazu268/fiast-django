from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label="タイトル")
    content = forms.CharField(label="本文", widget=forms.Textarea())
    image = forms.ImageField(label="イメージ画像", required=False)