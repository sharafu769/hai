from django.contrib import admin
from .models import CustomUser,TeacherProfile,StudentProfile,AdminProfile
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(AdminProfile)

