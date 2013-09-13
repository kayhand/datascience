from django.contrib import admin
from dscience.models import Topic
from dscience.models import Presentation
from dscience.models import Group
from dscience.models import UserProfile
from dscience.models import Assignment
from dscience.models import Homework
from dscience.models import Document
from dscience.models import Feedback

admin.site.register(Topic)
admin.site.register(Presentation)
admin.site.register(Group)
admin.site.register(UserProfile)
admin.site.register(Assignment)
admin.site.register(Homework)
admin.site.register(Document)
admin.site.register(Feedback)
