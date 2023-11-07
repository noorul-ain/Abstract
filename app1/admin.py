from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display =['name','email','password','Qualification','Experiance','City']

admin.site.register(Student)
admin.site.register(Teacher)




# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name','email','password','Class','Total_marks','Obtain_marks',' Board']
    
    
