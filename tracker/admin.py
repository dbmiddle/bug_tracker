from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker.models import MyUser
from tracker.models import Ticket

# Register your models here.
admin.site.register(MyUser, UserAdmin)
admin.site.register(Ticket)
