from django.contrib import admin
from feedApp.models import Course, Batch, Registration,Feedback
# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Registration)
# class Feed_admin(admin.ModelAdmin):
admin.site.register(Feedback)