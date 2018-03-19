# views.py 

# contains all functions that handle client-server communications, i.e. 
# contains functions that take in a web request and return a web response 

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib
import base64

from .models import Dorm
from .models import Review
from .forms import ReviewForm

# function to render the about page 
def about(request):
    template = loader.get_template('reviews/about.html')

    return render(request, 'reviews/about.html')

# function to render the index/map page  
def map(request):
	template = loader.get_template('reviews/map.html')
	dorms_list = Dorm.objects.order_by('name')
	context = {
		'dorms_list': dorms_list,
	}

	return render(request, 'reviews/map.html', context)

# function to render the page that allows users to look up dorm info and reviews 
def dorm_search(request):
	dorms_list = Dorm.objects.order_by('name')
	template = loader.get_template('reviews/dorm_search.html')
	context = {
		'dorms_list': dorms_list,
	}

	return render(request, 'reviews/dorm_search.html', context)

# function to render the page that contains the review and relevant information
# for a specific dorm queried by the user  
def dorm_reviews(request, dorm_id):
	dorm_queried = Dorm.objects.get(dorm_id=dorm_id)
	review_queried = Review.objects.filter(dorm=dorm_queried)
	template = loader.get_template('reviews/dorm_reviews.html')
	context = {
		'dorm_queried': dorm_queried,
		'review_queried':review_queried,
	}

	return render(request, 'reviews/dorm_reviews.html', context)

def review(request):
	template = loader.get_template('reviews/review.html')
	dorms_list = Dorm.objects.order_by('name')
	context = {
		'dorms_list': dorms_list,
	}
	return render(request, 'reviews/review.html', context)

# function to allow users to post reviews for a specific dorm 
# queries dorm by id and then stores the django form values into the database 
def post_review(request, dorm_id):
    dorm_to_review = Dorm.objects.get(dorm_id=dorm_id)
    template = loader.get_template('reviews/post_review.html')
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.dorm = dorm_to_review
            review.user = request.user.last_name;
            review.save()
            # store the form values into the database 
            return HttpResponseRedirect('/%s/' % dorm_id)
    else:
        form = ReviewForm()	

    context = {
        'dorm_to_review': dorm_to_review,
        'form': form,
    }

    return render(request, 'reviews/post_review.html', context)

def edit_review(request, review_id):
    review_to_edit = Review.objects.get(review_id=review_id)
    template = loader.get_template('reviews/edit_review.html')
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review_to_edit)
        if form.is_valid():
            review = form.save(commit=False)
            review.dorm = review_to_edit.dorm
            review.user = request.user.last_name
            review.save()
            return HttpResponseRedirect('/%s/' % review_to_edit.dorm.dorm_id)
    else:
        form = ReviewForm()

    context = {
        'review_to_edit': review_to_edit,
        'form': form,
    }            

    return render(request, 'reviews/edit_review.html', context)

def delete_review(request, review_id):
    review_to_delete = Review.objects.get(review_id=review_id)
    redirect_dorm_id = review_to_delete.dorm.dorm_id
    review_to_delete.delete()  
    return HttpResponseRedirect('/profile')  


# GET api route for retrieving information related to a specific dorm 
# Returns dorm information as a JSON object 
def api_dorms(request):
    dorms_list = Dorm.objects.order_by('name')
    
    response = []
    for dorm in dorms_list:
        dorm_json = {}
        dorm_json['name'] = dorm.name
        dorm_json['dorm_id'] = dorm.dorm_id
        dorm_json['address'] = dorm.address
        dorm_json['gender_policy'] = dorm.gender_policy
        dorm_json['bathroom_style'] = dorm.bathroom_style
        dorm_json['room_style'] = dorm.room_style
        dorm_json['amenities'] = dorm.amenities
        dorm_json['class_years'] = dorm.class_years
        dorm_json['comments'] = dorm.comments
        dorm_json['handicap_access'] = dorm.handicap_access
        dorm_json['custodial_services'] = dorm.custodial_services
        dorm_json['created_at'] = dorm.created_at
        dorm_json['updated_at'] = dorm.updated_at
        response.append(dorm_json)
    
    return JsonResponse(response, safe = False);
    
# GET API route for retrieving all the user reviews for a specific dorm
# Returns user reviews as a JSON object 
def api_dorm_reviews(request, dorm_id):
    dorm = Dorm.objects.get(dorm_id=dorm_id)
    reviews_list = Review.objects.filter(dorm=dorm)
    
    response = []
    for review in reviews_list:
        review_json = {}
        review_json['rating'] = review.rating
        review_json['handicap_rating'] = review.handicap_rating
        review_json['competetiveness'] = review.competetiveness
        review_json['review_id'] = review.review_id
        review_json['profile_id'] = review.profile_id
        review_json['room_type'] = review.room_type
        review_json['floor'] = review.floor
        review_json['title'] = review.title
        review_json['comment'] = review.comment
        review_json['created_at'] = review.created_at
        review_json['updated_at'] = review.updated_at
        response.append(review_json)
        
    return JsonResponse(response, safe = False);


# POST API route that allows users to post reviews for a specific dorm 
@csrf_exempt
def api_post_review(request):
		
    if request.method == 'POST':
        if 'user_token' not in request.POST:
            return HttpResponse("user_token is required", status=400);
        
        user_token = request.POST.get('user_token');
        
        # authenticate user token 
        try:
            user = User.objects.get(last_name=user_token);
        except ObjectDoesNotExist:
            return HttpResponse("User does not exist. Please provide a valid user_token or register", status=400);
        
        if 'dorm_id' not in request.POST:
            return HttpResponse("dorm_id is required", status=400);
        
        #athenticate dorm_id
        try:
            dorm_id = int(request.POST.get('dorm_id'))
            dorm_to_review = Dorm.objects.get(dorm_id=dorm_id)
        except ValueError:
            return HttpResponse("dorm_id must be an integer value", status=400)
        except ObjectDoesNotExist:
            return HttpResponse("Dorm does not exist. Please provide a valid dorm_id", status=400)
        
        if (('rating' not in request.POST) or ('handicap_rating' not in request.POST) or ('competetiveness' not in request.POST)):
            return HttpResponse("rating, handicap_rating, and competetiveness are required", status=400);
        
        try:
            dorm_rating = int(request.POST.get('rating'))
            dorm_handicap_rating = int(request.POST.get('handicap_rating'))
            dorm_competetiveness = int(request.POST.get('competetiveness'))
            
            # authenticate all ratings and competetiveness values 
            if ((dorm_rating < 1 or dorm_rating > 5) or (dorm_handicap_rating < 1 or dorm_handicap_rating > 5) or (dorm_competetiveness < 1 or dorm_competetiveness > 5)):
                return HttpResponse("rating, handicap_rating, and competetiveness must be in the range 1 to 5", status=400)
        except ValueError:
            return HttpResponse("rating, handicap_rating, and competetiveness must be integer values", status=400)
        
        if (('room_type' not in request.POST) or ('floor' not in request.POST) or ('title' not in request.POST) or ('comment' not in request.POST)):
            return HttpResponse("room_type, floor, title, and comment are required", status=400);
        
        room_type = request.POST.get('room_type')
        floor = request.POST.get('floor')
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        
        # check to ensure that room type, floor, title and comment have been inserted
        if ((room_type == '') or (floor == '') or (title == '') or (comment == '')):
            return HttpResponse("room_type, floor, title, and comment cannot be blank", status=400);
            
        review_obj = Review(user=user_token, dorm=dorm_to_review, rating=dorm_rating, handicap_rating=dorm_handicap_rating, competetiveness=dorm_competetiveness, room_type=room_type, floor=floor, title=title, comment=comment)
        review_obj.save()

        return HttpResponse("OK", status=200)
    else:
        return HttpResponse("Got GET request instead of POST", status=400)

# function to handle the signup request 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=raw_password)
            
            # hash username and password as token
            hash = hashlib.md5((username + raw_password).encode())
            hash_b64 = base64.b64encode(hash.digest())
            user.last_name = hash_b64;
            user.first_name = hash_b64;
            user.save();
            
            login(request, user)
            return redirect('home_map')
    else:
        form = UserCreationForm()
    return render(request, 'reviews/signup.html', {'form': form}, RequestContext(request))


# function to render the user profile page     
def profile(request):
    template = loader.get_template('reviews/profile.html')
    review_queried = Review.objects.filter(user=request.user.last_name)
    
    context = {
        'review_queried':review_queried,
    }
    
    return render(request, 'reviews/profile.html', context)