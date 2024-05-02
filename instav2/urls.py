from django.urls import path
from .import views

urlpatterns=[
    path('',views.log_in,name='login'),
    path('sign_up/',views.registration,name='sign_up'),
    path('home/(?P<pk>)/',views.home_page,name='home'),
    path('new_post/(?P<pk>)',views.posts,name='newpost'),
    path('edit/(?P<pk>)/',views.edit_profile,name='edit'),
    path('delt/(?P<pk>)/',views.delete_acc,name='del'),
    path('feed/(?P<pk>/',views.feed,name='feed'),
    path('logout/',views.log_out,name='logout'),
    path('like/(?P<post_id>)/',views.LikeView,name='like_post'),
    path('comment/(?P<post_id>)/(?P<pk>)/',views.comment_view,name='comment')
]