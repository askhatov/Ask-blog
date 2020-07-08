from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from comment.models import Comment



User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)

	def search(self,query):
		lookup = (
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(slug__icontains=query) |
		    Q(user__first_name__icontains=query) |
		    Q(user__last_name__icontains=query) |
		    Q(user__username__icontains=query)
		    )

		return self.filter(lookup)


class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model,using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query)

# Create your models here.
class BlogPost(models.Model):#blogpost_set this will give us a queryset that in this model
	user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='image/',blank=True,null=True)
	title = models.CharField(max_length=120)
	slug   = models.SlugField(unique=True)#hello world -> hello-world
	content = models.TextField(null=True,blank=True)
	publish_date = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = BlogPostManager()

	class Meta:
		ordering = ['-pk','publish_date','updated','timestamp']# this makes the ordering of the components in the model go from high to low


	def get_absolute_url(self):
		return f"/blog/{self.slug}" #we use this as the url, the same for the others

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit/"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete/"

	def get_user_url(self):

		return f'account/'



	@property
	def comments(self):
		instance = self
		# print(instance)
		qs = Comment.objects.filter_by_instance(instance)
		# print(qs)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		print(content_type)
		return content_type
	

