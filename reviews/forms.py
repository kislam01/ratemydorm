# forms.py 
# generates a simple django ModelForm that allows users to post reviews for a specific dorm  

from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		exclude = ('profile_id','dorm','created_at','updated_at','review_id','user')


