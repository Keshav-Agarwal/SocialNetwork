from . import views
from django.conf.urls import url

app_name = 'collegespace'

urlpatterns = [
    # /register/   :   url for registering
    url(r'^register/$', views.register, name='register'),

    # /home/   :   home page
    url(r'^home/$', views.home, name='home'),

    # /login_user/   :   to login
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /logout_user/   :   to logout
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /search/   :   to search a user
    url(r'^search/$', views.search, name='search'),

    # /profile/###   :   to view a profile
    url(r'^profile/(?P<prof_id>[0-9]+)/$', views.profile, name='profile'),

    # /add_friend/###   :   to add friend
    url(r'^add_friend/(?P<prof_id>[0-9]+)/$', views.add_friend, name='add_friend'),

    # /post_text/   :   to post text
    url(r'^post_text/$', views.post_text, name='post_text'),

    # /post_img/   :   to post text
    url(r'^post_img/$', views.post_img, name='post_img'),

    # /delete_post/###   :   to delete post
    url(r'^delete_post/(?P<post_id>[0-9]+)/$', views.delete_post, name='delete_post'),

    # /like_post/###   :   to like post
    url(r'^like_post/(?P<post_id>[0-9]+)/$', views.like_post, name='like_post'),

    # /delete_comment/###   :   to delete comment
    url(r'^delete_comment/(?P<comment_id>[0-9]+)/$', views.delete_comment, name='delete_comment'),

    # /like_comment/###   :   to like comment
    url(r'^like_comment/(?P<comment_id>[0-9]+)/$', views.like_comment, name='like_comment'),

    # /comment/   :   to comment
    url(r'^comment/', views.comment, name='comment'),
]
