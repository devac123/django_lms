import random
from faker import Faker
from django.core.management.base import BaseCommand
from LearnHub.models import Course, Module, Lesson, Assignment, Submission, Quiz, Question, Enrollment, InstructorProfile, Discussion
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.utils.dateparse import parse_datetime

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random data for models in bulk'

    def handle(self, *args, **kwargs):
        pass
        # Generate Users (Instructors and Students)
        # for i in range(1, 201):
        #     user = User.objects.create_user(
        #         username=fake.user_name(),
        #         email=fake.email(),
        #         password="password123",
        #         first_name=fake.first_name(),
        #         last_name=fake.last_name(),
        #     )

        #     # Add InstructorProfile for every second user (for simplicity)
        #     if i % 2 == 0:
        #         InstructorProfile.objects.create(
        #             user=user,
        #             profile_picture=fake.image_url()
        #         )

        # Generate Courses
        # for _ in range(100):
        #     course = Course.objects.create(
        #         title=fake.word() + " Course",
        #         discription=fake.text(),  # Ensure this matches the field name
        #         instructor_id=random.randint(163, 283),  # Random instructor
        #         start_date=fake.date_time_this_year(),
        #         end_date=fake.date_time_this_year(),
        #         category=fake.word()
        #     )

        # Generate Modules
        # for _ in range(100):
        #     module = Module.objects.create(
        #         title=fake.sentence(nb_words=3),
        #         course_id=random.randint(1, 100),
        #         order=random.randint(1, 10),
        #         description=fake.text(),
        #     )

        # Generate Lessons
        # for _ in range(100):
        #     lesson = Lesson.objects.create(
        #         title=fake.sentence(nb_words=3),
        #         content=fake.paragraph(),
        #         module_id=random.randint(1, 100),
        #         video_url=fake.url(),
        #         is_active=random.choice([True, False])
        #     )

        # Generate Assignments
        # for _ in range(100):
        #     assignment = Assignment.objects.create(
        #         title=fake.sentence(nb_words=3),
        #         description=fake.paragraph(),
        #         lesson_id=random.randint(1, 100),
        #         due_date=timezone.now() + timedelta(days=random.randint(1, 30)),
        #         total_marks=random.randint(50, 100)
        #     )

        # Generate Submissions
        # for _ in range(100):
        #     submission = Submission.objects.create(
        #         assignment_id=random.randint(1, 100),
        #         student_id=random.randint(163, 283),
        #         content=fake.text(),
        #         submission_date=timezone.now(),
        #         grade=random.randint(0, 100),
        #         feedback=fake.sentence()
        #     )

        # Generate Quizzes
        # for _ in range(100):
        #     quiz = Quiz.objects.create(
        #         title=fake.sentence(nb_words=3),
        #         lesson_id=random.randint(1, 100),
        #         total_marks=random.randint(10, 50)
        #     )

        # Generate Questions
        # for _ in range(100):
        #     question = Question.objects.create(
        #         quiz_id=random.randint(1, 100),
        #         text=fake.sentence(),
        #         option_1=fake.word(),
        #         option_2=fake.word(),
        #         option_3=fake.word(),
        #         option_4=fake.word(),
        #         correct_answer=random.choice(['option_1', 'option_2', 'option_3', 'option_4'])
        #     )

        # Generate Enrollments
        # for _ in range(100):
        #     enrollment = Enrollment.objects.create(
        #         student_id=random.randint(163, 283),
        #         course_id=random.randint(1, 100),
        #         enrollment_date=timezone.now()
        #     )

        # Generate Discussions
        # for _ in range(100):
        #     discussion = Discussion.objects.create(
        #         course_id=random.randint(1, 100),
        #         student_id=random.randint(163, 283),
        #         message=fake.sentence(),
        #         created_at=timezone.now()
        #     )

        # self.stdout.write(self.style.SUCCESS('Successfully generated 100 records for each model.'))
