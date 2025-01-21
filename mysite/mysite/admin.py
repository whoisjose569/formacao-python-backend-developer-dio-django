from django.contrib import admin

from polls.models import Choice, Question


class CustomAdminSite(admin.AdminSite):
    site_header = "Curso de Python Admin"


admin_site = CustomAdminSite()
admin_site.register(Choice)
admin_site.register(Question)