from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Full Name","size":"30"}),label='')
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
			'placeholder':'Email',
			"size":"30"
			}
			),
		label=''
		)
	content = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'Message','rows':4, 'cols':"33"}),label='')

	def clean_email(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		print(email)
		if email.endswith(".edu"):
			raise forms.ValidationError("This is not a valid email. Please do not use .edu")

		return email

class LoginForm(forms.Form):
	username      = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Username","size":"30"}),label='')
	password      = forms.CharField(
	                    required=False,
	                    widget=forms.PasswordInput(attrs={
	                    	"placeholder":"Password",

	                    	# "class":"new-class",
	                    	# "id":"my dash id for text area",
	                    	"rows":20,
	                    	"cols":120
	                    	}
	                    ),
	                    label=''
	                )


class RegisterForm(forms.Form):
	username      = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Your username","size":"30"}),label='')
	email    = forms.EmailField(
		widget=forms.EmailInput(
			attrs={'class':'form-control',
			'placeholder':'Email'
			}
			),
		label=''
		)
	password      = forms.CharField(
	                    required=False,
	                    widget=forms.PasswordInput(attrs={
	                    	"placeholder":"Your password"
	                    	}
	                    	),
	                    label=''
	                    )
	password2     = forms.CharField(
	                    required=False,
	                    widget=forms.PasswordInput(attrs={
	                    	"placeholder":"Confirm your password"
	                    	}
	                    ),
	                    label=''
	                )
	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username
	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email is taken")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords must match.")
		return data

# class ProfileForm(forms.Form):
#     ...
#     timezone = forms.ChoiceField(
#         label=_('Time Zone'),
#         choices=[(t, t) for t in pytz.common_timezones]
#     )