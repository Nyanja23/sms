from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='student_profile')

    registration_number = models.CharField(max_length=50,unique=True,db_index=True)

    date_of_birth =  models.DateField(blank=True,null=True)

    year_of_study = models.PositiveSmallIntegerField(default=1)

    program = models.ForeignKey("Program",on_delete=models.SET_NULL, null=True,blank=True, related_name='students')

    def __str__(self) -> str:
        return f"{self.registration_number} - {self.user.get_full_name() or self.user.username}"

class Program(models.Model):
    name = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=50,unique=True, db_index=True)
    duration_years = models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1),MaxValueValidator(10)])

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.code}"

class CourseUnit(models.Model):
    code = models.CharField(max_length=50,unique=True,db_index=True)
    title = models.CharField(max_length=150)
    credit_units = models.PositiveSmallIntegerField(default=3,validators=[MinValueValidator(3),MaxValueValidator(10)])

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.title}"

SEMESTER_CHOICES = (
    (1,'Semester One'),
    (2,'Semester Two'),
)

class ProgramCourse(models.Model):
    program = models.ForeignKey(Program,on_delete=models.CASCADE,related_name='program_courses')
    course_unit = models.ForeignKey(CourseUnit,on_delete=models.CASCADE,related_name='program_courses')
    year_offered = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)

    is_core = models.BooleanField(default=True)

    class Meta:
        unique_together = [
            ['program','course_unit']
        ]

        indexes = [
            models.Index(fields=['program','year_offered','semester'])
        ]

    def __str__(self):
        return f"{self.program.code} - {self.course_unit.code} (Y{self.year_offered} S{self.semester})"
    