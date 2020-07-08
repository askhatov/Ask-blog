from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogPost
from django.contrib import messages
from urllib.parse import quote_plus
from django.utils import timezone

from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
# https://stackoverflow.com/questions/25179386/django-how-to-count-number-of-people-viewed
from django.http import Http404
from .forms import BlogPostForm, BlogPostModelForm

from comment.forms import CommentForm
# from django.utils import timezone
# Create your views here.

#GET->1 object
#filter -> [] objects 


def blog_post_list_view(request):
	# This is the list of items we we have in our blog app. So we assign all the objects of BlogPost app and send it to the html file
	# list our objects
	# could be search
	# qs = BlogPost.objects.filter(title__icontains='obj').all() could be used to filter specific titles that we want
	# now = timezone.now()
	qs = BlogPost.objects.all().published() #queryset -> list of python objects
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct() # we used distinct so the same post would not be posted twice
	# qs = BlogPost.objects.filter(publish_date__lte=now)# video number 53
	template_name = 'blog/list.html'
	context = {'object_list':qs}

	return render(request,template_name,context)


@login_required
# @staff_member_required
def blog_post_create_view(request):
	
	form = BlogPostModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		print(form.cleaned_data)
		
		obj = form.save(commit=False)
		obj.user = request.user
		obj.title = form.cleaned_data.get('title')# + "0"
		obj.save()
		return redirect('/')
		form = BlogPostModelForm
	template_name = 'blog/create.html'
	context = {'form':form}
	return render(request,template_name,context)

def blog_post_detail_view(request,slug):
	# 1 objects -> detail view
	instance = get_object_or_404(BlogPost, slug=slug)
	# com = get_object_or_404(Comment,slug=slug)
	# if instance.publish_date > timezone.now().date() or instance.draft:
	# 	if not request.user.is_staff or not request.user.is_superuser:
	# 		raise Http404
	share_string = quote_plus(instance.content)

	initial_data = {
	'content_type':instance.get_content_type,
	'object_id':instance.id
	}
	form = CommentForm(request.POST or None,initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get('content_type')
		content_type = form.cleaned_data.get('content_type')
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get('content')
		new_comment,created = Comment.objects.get_or_create(
			user = request.user,
			content_type = content_type,
			object_id = obj_id,
			content   = content_data
			)
		if created:
			print('Yeah it worked')
	comments = instance.comments
	template_name = 'blog/detail.html'
	context = {
	"object":instance,
	'comments': comments,
	'share_string':share_string,
	'comment_form':form
	}

	return render(request,template_name,context)



# @staff_member_required
@login_required
def blog_post_update_view(request,slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'blog/update.html'
	context = {'form':form,'title':f"Update {obj.title}"}

	return render(request,template_name,context)


# @staff_member_required
@login_required
def blog_post_delete_view(request,slug):  # This makes people to log in before opening the page
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/delete.html'
	print(request)
	if request.method == "POST":
		obj.delete()
		return redirect('/blog')
	context = {"object":obj}

	return render(request,template_name,context)



