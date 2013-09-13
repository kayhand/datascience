# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone

from dscience.models import Topic, Group, UserProfile, Assignment, Homework, Feedback
from dscience.forms import PresentationForm, DocumentForm, AssignmentForm, MyAssignmentForm, FeedbackForm

@login_required
def index(request):
    topic_list = Topic.objects.order_by("name")
    context = RequestContext(request, {
          'topic_list': topic_list,
    })
    return render(request, 'dscience/index.html', context)

@login_required
def presentation(request):
    #everything = Group.objects.all()
    uProfile = UserProfile.objects.select_related().get(user = request.user)

    if request.method == 'POST':
        form = PresentationForm(request.POST, request.FILES)
        first_due = uProfile.group.presentation.first_due_date;
        if form.is_valid():
            if first_due > timezone.now():
                print "late"
                uProfile.group.presentation.pFile = request.FILES['presFile']
                uProfile.group.presentation.save()
            
                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('dscience.views.presentation'))
            else:
                return HttpResponseRedirect(reverse('dscience.views.latePUpload'))
    else:
        form = PresentationForm() # A empty, unbound form

    # Load documents for the list page
    documents = uProfile.group.presentation.pFile;

    # Render list page with the documents and the form
    return render_to_response(
        'dscience/presentation.html',
        {'documents': documents, 'form': form, 'uProfile': uProfile},
        context_instance=RequestContext(request)
                              )

@login_required
def assignment(request):
    try:
        uProfile = UserProfile.objects.select_related().get(user = request.user)
    except UserProfile.DoesNotExist:
        uProfile = None

    try:
        assignInfo = Assignment.objects.get(group=uProfile.group)
    except Assignment.DoesNotExist:
        assignInfo = None

    context = RequestContext(request, {
                             'uProfile': uProfile,
                             'assignInfo': assignInfo,
                             })

    if request.method == 'POST' and not (assignInfo == None):
        form = AssignmentForm(request.POST, request.FILES)
        first_due = assignInfo.upload_due_date;
        if form.is_valid():
            if first_due > timezone.now():
                assignInfo.file = request.FILES['assignfile']
                assignInfo.due_date = request.POST['dueDate']
                assignInfo.save()
                return HttpResponseRedirect(reverse('dscience.views.assignment'))
            else:
                return HttpResponseRedirect(reverse('dscience.views.latePUpload'))

    elif assignInfo:
        form = AssignmentForm(initial={'dueDate': str(assignInfo.due_date).split(" ")[0]})
    else:
        form = AssignmentForm()
    return render_to_response('dscience/assignment.html', {'uProfile': uProfile, 'assignInfo': assignInfo, 'form': form }, context_instance=RequestContext(request))

@login_required
def myassignments(request):
    try:
        uProfile = UserProfile.objects.select_related().get(user = request.user)
    except UserProfile.DoesNotExist:
        uProfile = None
    
    try:
        myAssignInfo = Assignment.objects.exclude(group=uProfile.group)            
    except Assignment.DoesNotExist:
        myAssignInfo = None
    
    return render_to_response('dscience/myassignments.html', {'myAssignInfo': myAssignInfo }, context_instance=RequestContext(request))

@login_required
def myassignmentdetail(request, asgn_id):
    uProfile = UserProfile.objects.get(user=request.user)
    asgn = get_object_or_404(Assignment, pk=asgn_id)
    
    try:
        homew = Homework.objects.get(user=uProfile, assignment = asgn)
    except Homework.DoesNotExist:
        homew = None
    
    if request.method == 'POST' and not (asgn == None):
        form = MyAssignmentForm(request.POST, request.FILES)
        due = asgn.due_date;
        if form.is_valid():
            if due > timezone.now():
                now = datetime.now()
                
                if(homew):
                    print "update"
                    homew.upload_date = now
                    homew.file=request.FILES['myassignfile']
                    homew.save()
                else:
                    
                    hmw = Homework(assignment=asgn, user=uProfile, upload_date=now, file=request.FILES['myassignfile'])
                    hmw.save()
                return HttpResponseRedirect(reverse('dscience.views.myassignments'))
            else:
                return HttpResponseRedirect(reverse('dscience.views.latePUpload'))
    
    else:
        form = MyAssignmentForm()
    return render_to_response('dscience/asgndetail.html', {'asgn': asgn, 'form': form, 'homew': homew }, context_instance=RequestContext(request))

@login_required
def givefeedback(request):
    #everything = Group.objects.all()
    uProfile = UserProfile.objects.select_related().get(user = request.user)
    #Get all the feedbacks this user needs to give
    feedbackInfo = Feedback.objects.filter(user_giving_feedback = uProfile, is_given = 0)
    
    return render_to_response('dscience/givefeedback.html', {'uProfile' : uProfile, 'fInfo': feedbackInfo }, context_instance= RequestContext(request))

@login_required
def feedbackdetail(request, feed_id):
    uProfile = UserProfile.objects.get(user=request.user)
    feedback = get_object_or_404(Feedback, pk=feed_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        due = feedback.due_date;
        if form.is_valid():
            if due > timezone.now():
                now = datetime.now()
                feedback.upload_date = now
                feedback.is_given = 1
                #Create form with post data
                f = FeedbackForm(request.POST, instance = feedback)
                f.save()
                messageText = 'Feedback for ' + str(feedback.user_getting_feedback) + ' for the presentation ' + str(feedback.presentation.topic.name) +' is given succesfully!'
                messages.success(request, messageText)
                return HttpResponseRedirect(reverse('dscience.views.givefeedback'))
            else:
                return HttpResponseRedirect(reverse('dscience.views.latePUpload'))
                    

    else:
        form = FeedbackForm()
    return render_to_response('dscience/feedbackdetail.html', {'uProfile': uProfile, 'feedback': feedback, 'form': form}, context_instance=RequestContext(request))


@login_required
def myfeedbacks(request):
    #everything = Group.objects.all()
    uProfile = UserProfile.objects.select_related().get(user = request.user)
    #Get all the feedbacks this user needs to give
    feedbacks = Feedback.objects.filter(user_getting_feedback = uProfile, is_given = 1)
    
    return render_to_response('dscience/myfeedbacks.html', {'uProfile' : uProfile, 'fInfo': feedbacks }, context_instance= RequestContext(request))

@login_required
def latePUpload(request):
    return render(request, 'dscience/lateUpload.html')

@login_required
def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'dscience/detail.html', {'topic': topic})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def logout_page(request):
    """
        Log users out and re-direct them to the main page.
        """
    logout(request)
    return HttpResponseRedirect('/login/')