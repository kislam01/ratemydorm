# urls.py 
# contains list of urls for the website 

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static 

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.map, name='home_map'),
    url(r'^dorm_search/$', views.dorm_search, name='dorm_search'),
    url(r'^(?P<dorm_id>[0-9]+)/$', views.dorm_reviews, name='dorm_reviews'),
    url(r'^(?P<dorm_id>[0-9]+)/post/$', views.post_review, name='post_review'),
    url(r'^(?P<review_id>[0-9]+)/delete/$', views.delete_review, name='delete_review'),
    url(r'^(?P<review_id>[0-9]+)/edit/$', views.edit_review, name='edit_review'),
    url(r'^map/$', views.map, name='map'),
    url(r'^review/$', views.review, name='review'),
    url(r'^about/$', views.about, name='about'),
    url(r'^api/dorms/$', views.api_dorms, name='api_dorms'),
    url(r'^api/reviews/(?P<dorm_id>[0-9]+)/$', views.api_dorm_reviews, name='api_dorm_reviews'),
    url(r'^api/post/$', views.api_post_review, name='api_post_review'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

