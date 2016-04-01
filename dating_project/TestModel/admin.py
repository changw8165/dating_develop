from django.contrib import admin
from TestModel.models import CourseDetails
from TestModel.models import contact,tag
# Register your models here.
#admin.site.register(CourseDetails)

#default format
#admin.site.register([Contact, Tag])

#self defined format
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',),
            'fields': ('age',),
        }]
    )

admin.site.register(contact, ContactAdmin)
admin.site.register([CourseDetails, tag])