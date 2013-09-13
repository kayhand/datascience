from django.conf.urls import patterns, url
from django.conf import settings

from dscience import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^presentation/$', views.presentation, name='presentation'),
    url(r'^presentation/latePUpload/$', views.latePUpload, name='latePUpload'),
    url(r'^assignment/$', views.assignment, name='assignment'),
    url(r'^myassignments/$', views.myassignments, name='myassignments'),
    url(r'^myassignments/(?P<asgn_id>\d+)/$', views.myassignmentdetail, name='myassignmentdetail'),
    url(r'^feedback/$', views.givefeedback, name='givefeedback'),
    url(r'^feedback/(?P<feed_id>\d+)/$', views.feedbackdetail, name='feedbackdetail'),
    url(r'^myfeedbacks/$', views.myfeedbacks, name='myfeedbacks'),
    # ex: /polls/5/
    url(r'^(?P<topic_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<topic_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<topic_id>\d+)/vote/$', views.vote, name='vote'),
    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                        {'next_page': '../login/'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                        'document_root': settings.MEDIA_ROOT,
    }),
                       
)
