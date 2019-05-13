from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
import datetime
from .models import Friends, ImagePost, Posts, TextPost, Comments
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


# Registering
# messaging

@login_required
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'collegespace/login.html')
    else:
        message = request.user.username
        posts = get_posts()
        return render(request, 'collegespace/home.html', {
            'message': message,
            'posts': posts,
        })


@login_required
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'collegespace/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                message = username
                return render(request, 'collegespace/home.html', {
                    'message': message,
                    'posts': get_posts(),
                })
            else:
                return render(request, 'collegespace/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'collegespace/login.html', {'error_message': 'Invalid login'})
    return render(request, 'collegespace/login.html')


@login_required
def search(request):
    searched_str = request.GET.get("searched_str")
    print(searched_str)
    if searched_str:
        results = User.objects.filter(username__icontains=searched_str)
    else:
        results = User.objects.all()
    return render(request, "collegespace/result.html", {
        'results': results
    })


@login_required
def profile(request, prof_id):
    user = get_object_or_404(User, pk=prof_id)
    return render(request, 'collegespace/profile.html', {
        'user': user,
    })


# to be completed
def register(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            username = u_form.cleaned_data['username']
            password = p_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = request.user.username
                    return render(request, 'collegespace/home.html', {
                        'message': message,
                        'posts': get_posts(),
                    })
        return render(request, 'collegespace/login.html')
    else:
        u_form = UserForm(instance=request.user)
        # p_form = ProfileForm(instance=request.user.profile)
        return render(request, 'collegespace/login.html', {
            'u_form': u_form,
        })


@login_required
def add_friend(request, prof_id):
    user_friends = Friends.objects.filter(user=request.user, friend=prof_id)
    if len(user_friends) == 0:
        friend = Friends(user=request.user, friend=prof_id)
        friend.save()
    frnd_list_ = Friends.objects.filter(user=request.user)
    frnd_list = []
    for frnd in frnd_list_:
        friend = User.objects.get(pk=frnd.friend)
        frnd_list.append(friend)
    return render(request, 'collegespace/added.html', {
        'frnd_list': frnd_list,
    })


@login_required
def post_text(request):
    if request.method == "POST":
        text_post = TextPost()
        text_post.text = request.POST['post']
        text_post.user = request.user
        text_post.date_created = datetime.datetime.now()
        text_post.save()
        return render(request, 'collegespace/home.html')
    else:
        return render(request, 'collegespace/home.html')


@login_required
def post_img(request):
    if request.method == 'POST':
        img_post = ImagePost()
        img_post.pic = request.FILES['profilepic']
        img_post.description = request.POST['description']
        img_post.user = request.user
        img_post.date_created = datetime.datetime.now()
        img_post.save()

    return render(request, 'collegespace/uploadphoto.html')


def get_posts():
    posts_to_return = []
    posts = Posts.objects.order_by('-date_created')
    for post in posts:
        a = TextPost.objects.filter(posts_ptr_id=post.id)
        if len(a) == 0:
            a = ImagePost.objects.filter(posts_ptr_id=post.id)
        for b in a:
            posts_to_return.append(b)
    return posts_to_return


@login_required
def delete_post(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
        post.delete()
        return render(request, 'collegespace/home.html')
    except ObjectDoesNotExist:
        return render(request, 'collegespace/home.html')


@login_required
def like_post(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return render(request, 'collegespace/home.html')
    except ObjectDoesNotExist:
        return render(request, 'collegespace/home.html')


@login_required
def delete_comment(request, comment_id):
    try:
        cmnt = Comments.objects.get(pk=comment_id)
        cmnt.delete()
        return render(request, 'collegespace/home.html')
    except ObjectDoesNotExist:
        return render(request, 'collegespace/home.html')


@login_required
def like_comment(request, comment_id):
    try:
        cmnt = Comments.objects.get(pk=comment_id)
        cmnt.likes += 1
        cmnt.save()
        return render(request, 'collegespace/home.html')
    except ObjectDoesNotExist:
        return render(request, 'collegespace/home.html')


@login_required
def comment(request):
    if request.method == "POST":
        cmnt = request.POST['comment']
        post = Posts.objects.get(pk=int(request.POST['post']))
        print("----------" + str(post.likes))
        c = Comments()
        c.comment_text = str(cmnt)
        c.post = post
        c.save()
    return render(request, 'collegespace/home.html')