from django import forms
from .models import Account
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountModelForm(forms.ModelForm):

	class Meta:
		model = Account
		# fields = ['name','slug','image','desc','address_one','address_two','city','state','phone','user']
		fields = ['image']
	# def clean_user(self):
	# 	user = self.cleaned_data.get('user')
	# 	qs = User.objects.filter(account=user)
	# 	if qs.exists():
	# 		return render(request,'home.html')