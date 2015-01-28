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
def testlogin(request):
    return render(request, 'testlogin.html')

def input(request):
    return render(request, 'input.html')

def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        return redirect(list_)
    return render(request, 'list.html', {'list': list_})

def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    list_.shared_with.add(request.POST['email'])
    return redirect(list_)

