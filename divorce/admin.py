from django.contrib import admin
from divorce.models import Divorce

# Register your models here.
class DivorceAdmin(admin.ModelAdmin):
    model = Divorce
    list_display = ['name','State_issued_divorce_id','Date_of_birth','Nationality','Maritial_status','Highest_education']
    search_fields=('name','State_issued_divorce_id','Date_of_birth','Nationality','Maritial_status','Highest_education') 
admin.site.register(Divorce,DivorceAdmin)

