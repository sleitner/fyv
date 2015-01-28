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
def analytics(request):
    return render(request, 'analytics.html')
#######junk
def testlogin(request):
    return render(request, 'testlogin.html')
def input(request):
    return render(request, 'input.html')
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
    twitter_friends_list =  get_twitter_friends(request)
    if request.user:
        print('!!!s!!!!!')
    if not request.user.is_authenticated():
        return render(request, 'home.html')
    print(twitter_friends_list)
    #context = {'twitter_friends_list': get_twitter_friends(request)}
    #template = 'members.html'
    
#    List.create_new(item_firstname=twitter_friend['firstname'],
#                    item_lastname=twitter_friend['lastname'],
#                    )
#    list_ = form.save(owner=request.user)
#    return redirect(list_)
    #return render(request, template, context)
    return redirect('home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('/')
    



