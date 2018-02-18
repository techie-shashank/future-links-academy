from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class Post(models.Model):
	owner       = models.ForeignKey(User)
	title 		= models.CharField(max_length=100)
	category 	= models.CharField(max_length = 25)
	description = models.CharField(max_length = 5000)
	timestamp 	= models.DateTimeField( auto_now_add = True )
	Updated 	= models.DateTimeField( auto_now = True )
	slug 		= models.SlugField( null=True,blank=True )
	likes 		= models.ManyToManyField(User, related_name='likes')
	pic 		= models.FileField(blank=True, null=True)

	@property
	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:postdetail',kwargs={ 'slug': self.slug })

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Post)

class Comments(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.text



