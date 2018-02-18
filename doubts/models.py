from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Question(models.Model):
	content 	= models.CharField(max_length= 500)
	slug 		= models.SlugField( null=True,blank=True )
	votes  		= models.ManyToManyField(User, related_name='votes')
	timestamp	= models.DateTimeField(auto_now_add= True)
	subject		= models.CharField(max_length=500,default='others')

	@property
	def total_votes(self):
		return self.votes.count()
	
	def get_absolute_url(self):
		return reverse('doubts:Questiondetail',kwargs={ 'slug': self.slug })

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Question)

class Answers(models.Model):
	question 	= models.ForeignKey(Question)
	text     	= models.CharField(max_length=5000)
	upvotes  	= models.ManyToManyField(User, related_name='upvote')
	timestamp	= models.DateTimeField(auto_now_add= True)

	@property
	def total_upvotes(self):
		return self.upvotes.count()