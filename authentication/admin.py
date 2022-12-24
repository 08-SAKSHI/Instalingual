from django.contrib import admin
from authentication.models import RegisterUser
# Register your models here.

#admin.site.register(RegisterUser)
@admin.register(RegisterUser)
class RegisterAdmin(admin.ModelAdmin):
 list_display = ['new_user','gender','DOB','occupation','mother_tongue','phone_number','Future_goals']