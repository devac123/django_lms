from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    childrens = models.ManyToManyField('self', null=True, blank=True, symmetrical=False, related_name='children')

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=100)
    menuItems = models.ManyToManyField(MenuItem, related_name='menus')

    def __str__(self):
        return self.title


class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='instructors/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    
class Course(models.Model):
    title = models.CharField(max_length=555)
    discription = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE,related_name="courses")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class Module(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    order = models.PositiveIntegerField(default=0)
    description = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")
    video_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
    

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="assignments")
    due_date = models.DateTimeField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='submissions/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    grade = models.PositiveIntegerField(null=True, blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"
    

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="quizzes")
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
    

class Discussion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="discussions")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Discussion by {self.student.username} in {self.course.title}"