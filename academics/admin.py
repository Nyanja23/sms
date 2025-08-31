from django.contrib import admin
from .models import StudentProfile,Program,ProgramCourse,CourseUnit

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    search_fields = ('registration_number','user_name','user_email')
    list_display = ('registration_number','user','year_of_study')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    search_fields = ('name','code')
    list_display = ('name','code','duration_years')

@admin.register(CourseUnit)
class CourseUnitAdmin(admin.ModelAdmin):
    search_fields = ('code','title')
    list_display = ('code','title','credit_units')

@admin.register(ProgramCourse)
class ProgramCourseAdmin(admin.ModelAdmin):
    list_display = ('program','course_unit','year_offered','semester','is_core')
    list_filter = ('program','year_offered','semester','is_core')