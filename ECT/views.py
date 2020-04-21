from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Meeting, Member
from .forms import MemberForm
# Create your views here.
#class IndexView(generic.ListView):
def index(request):

    data = Member.objects.all()
    Meeting_list = Meeting.objects.order_by()
    context = {
        'Meeting_list' : Meeting_list,
        'data':data
        }
    return render(request, 'ECT/index.html', context)

def detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'ECT/detail.html', {'meeting': meeting})

def create(request):

    if request.method =='POST':
        obj = Member()
        member = MemberForm(request.POST, instance = obj)
        member.save()
        return redirect(to='/ECT')
    
    params = {
        'title' : 'Ourteam members',
        'form': MemberForm(),
    }

    return render(request, 'ECT/create.html', params)

def edit(request, num):
    obj = Member.objects.get(id=num)
    if request.method=='POST':
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/ECT')
    params = {
        'title' :'Members',
        'id' : num,
        'form' : MemberForm(instance = obj),
    }
    return render(request, 'ECT/edit.html', params)