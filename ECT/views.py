from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Meeting
# Create your views here.
#class IndexView(generic.ListView):
def index(request):
    Meeting_list = Meeting.objects.order_by()
    context = {'Meeting_list' : Meeting_list}
    return render(request, 'ECT/index.html', context)

def detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'ECT/detail.html', {'meeting': meeting})
