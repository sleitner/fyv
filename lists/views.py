from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

User = get_user_model()

from lists.forms import ItemForm, NewListForm
from lists.models import List

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})
def faq(request):
    return render(request, 'FAQ.html')
def motivation(request):
    return render(request, 'motivation.html')
def modeling(request):
    return render(request, 'modeling.html')
#######junk
def testlogin(request):
    return render(request, 'testlogin.html')
def overview(request):
    return render(request, 'overview.html')
def slides(request):
    return render(request, 'slides.html')
#######^junk

def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid(): #this is a django form built-in for checking required
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        return redirect(list_)
    return render(request, 'list.html', {'list': list_})

from django.contrib.auth import logout as auth_logout
from lists.socialnetworks.twitter import get_twitter_friends
from lists.models import List
def new_member_list(request):
    context = {}
    twitter_result =  get_twitter_friends(request)
    if isinstance(twitter_result,str):
        return render(request, 'twitter_error.html',{'err': twitter_result})
    else:
        twitter_friends_list = twitter_result
    if not request.user.is_authenticated():
        return render(request, 'home.html')
    list_ = ''
    for tfriend in twitter_friends_list:
        list_ = List.create_new_twitt(tfriend['username'],
                                tfriend['firstname'],
                                tfriend['lastname'],
                                item_zipcode='', 
                                list_=list_,
                                )
    return render(request, 'list.html', {'list': list_})

def logout_view(request):
    auth_logout(request)
    return redirect('/')
    



