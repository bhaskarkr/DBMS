from django import forms
from MOVIE_REVIEW.models import comments

class addcomment(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 3,}))
    #points = forms.IntegerField(widget=forms.IntegerField(attrs={'placeholder':'enter between 0 to 10',}))
    class Meta:
        model=comments
        fields=['email','mov_id','points','comment',]
        widgets = {'mov_id':forms.HiddenInput(attrs={'value':1}),}
        #widgets = {'comment':forms.Textarea(attrs={'rows':5,'cols':80}),}