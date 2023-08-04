from django.contrib import admin
from .models import User
# from import_export.admin import ImportExportModelAdmin
from import_export.admin  import ImportExportModelAdmin

# Register your models here.

class UserColumns(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["username", "email", "password", "career", "location", "created"]
    


admin.site.register(User, UserColumns)