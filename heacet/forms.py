from django import forms
from .models import Nogizaka, Message

class HeacetForm(forms.Form):
	name = forms.CharField(label="名前")
	mail = forms.EmailField(label="メールアドレス")
	gender = forms.BooleanField(label="性別",required="False")
	age = forms.IntegerField(label="年齢")
	birthday = forms.DateField(label="誕生日")

class NogizakaForm(forms.ModelForm):
	class Meta:
		model = Nogizaka
		fields = ['name','mail','gender','age','birthday']

class FindForm(forms.Form):
	find = forms.CharField(label='検索', required=False)

class CheckForm(forms.Form):
	str = forms.CharField(label="String")

	def clean(self):
		cleaned_data = super().clean()
		str = cleaned_data['str']
		if(str.lower().startswith('no')):
			raise forms.ValidationError('You input "NO!"!')

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['title','content','friend']
