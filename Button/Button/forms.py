from django import forms

class tweezer_form(forms.Form):
 x1 = forms.DecimalField(label='x1')
 x2 = forms.DecimalField(label='x2')

class splint_form(forms.Form):
 x1 = forms.DecimalField(label='x1')
 x2 = forms.DecimalField(label='x2')
 x3 = forms.DecimalField(label='x3')

class clip_form(forms.Form):
 x1 = forms.DecimalField(label='x1')
