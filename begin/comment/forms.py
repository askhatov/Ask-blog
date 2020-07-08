from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	# content_type = forms.CharField(widget=forms.HiddenInput(attrs={
	# 	"placeholder": "Comment"}),
	# 	label=''
	# )
	# object_id    = forms.IntegerField(widget=forms.HiddenInput)
	# # parent_id    = forms.IntegerField(widget=forms.HiddenInput,required=False)
	# content      = forms.CharField(widget=forms.Textarea)
	# # class Meta:
	# # 	model = Comment
	# # 	fields = ('user','content','publish_date')

	class Meta:
		model = Comment
		fields = ('content_type', 'object_id', 'content')
		widgets = {
		'content_type': forms.HiddenInput,
		'object_id': forms.HiddenInput,
		}