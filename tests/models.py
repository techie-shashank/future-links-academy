from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL
 
class Test(models.Model):
	title 		= models.CharField(max_length=100)	
	timestamp 	= models.DateTimeField( auto_now_add = True )
	slug 		= models.SlugField( null=True,blank=True )
	time_limit	= models.CharField(max_length=300)
	subject		= models.CharField(max_length=300,default='other')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tests:testpaper',kwargs={ 'slug': self.slug })

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Test)

class Question(models.Model):
	test 	 		= models.ForeignKey(Test)
	question 		= models.TextField()
	option1	 		= models.CharField(max_length=300)
	option2  		= models.CharField(max_length=300)
	option3  		= models.CharField(max_length=300)
	right_answer 	= models.CharField(max_length=300)

	def __str__(self):
		return self.question


class Score(models.Model):
	user  			= models.ForeignKey(User)
	test 	 		= models.ForeignKey(Test)
	marks			= models.IntegerField()

	class Meta:
		ordering = ['-marks']



	

