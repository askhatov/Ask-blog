from django import forms
from .models import BlogPost,Comment

class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug  = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
	# title = forms.CharField()
	class Meta:
		model = BlogPost
		fields  = ['title','image','slug','content']
		# the difference between this model form and just forms is that model forms have fields that we want to include 	
	def clean_title(self,*args,**kwargs):
		print(dir(self))
		instance = self.instance
		print(instance)
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexact=title) # we use iexact so no matter how capitalized the words are, we still wont use that word
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		print(title)
		print(qs)
		if qs.exists():#This is show that our specific title exists in the database or not
			raise forms.ValidationError("This title already exists. Please use different title")
		return title


# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Comment
# 		fields = ('user','content','publish_date')