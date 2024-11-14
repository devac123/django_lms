from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Course, Enrollment, Assignment, Lesson, Submission, Question, Quiz, Menu

# View for the user's profile page, accessible only for logged-in users
@login_required
def profile_view(request):
    return render(request, 'user/profile.html')  

# View to display a list of all courses, with pagination
def cource_list(req):
    # Fetch all courses, but only return necessary fields for efficiency
    cource_list = Course.objects.all().values()

    # Default number of courses per page (6). If a custom page count is provided, use that instead
    paginator = Paginator(cource_list, 6)
    if req.GET.get('page_count'):
        paginator = Paginator(cource_list, req.GET.get('page_count'))

    # Get the page number from the URL, default to the first page
    page_number = req.GET.get('page')

    # Create a Page object for the requested page number
    page_obj = paginator.get_page(page_number)
    
    # Pass courses and pagination information to the template
    data = {
        "cources": list(cource_list),
        "page_title": "Cource Listing",
        "page_obj": page_obj
    }
    
    return render(req, 'CourceListing.html', data)

# View for displaying the details of a specific course
def course_detail(request, course_id):
    # Fetch the course object by its ID or return a 404 error if not found
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

# View to handle the course enrollment process
@login_required
def enroll_in_course(request, course_id):
    # Fetch the course object by its ID or return a 404 error if not found
    course = get_object_or_404(Course, pk=course_id)

    # Check if the student is already enrolled in the course
    if Enrollment.objects.filter(student=request.user, course=course).exists():
        # Render a page indicating the user is already enrolled
        return render(request, 'courses/already_enrolled.html', {'course': course})

    # Enroll the student in the course by creating an Enrollment object
    Enrollment.objects.create(student=request.user, course=course)

    # Redirect to the course detail page or a success page after enrollment
    return redirect('course_detail', course_id=course.id)


@login_required
def course_lessons(request, course_id):
    # Fetch the course object by its ID
    course = get_object_or_404(Course, id=course_id)

    # Get all the lessons related to the course (you could also apply ordering if needed)
    lessons = Lesson.objects.filter(module__course=course)

    # Pass the course and lessons to the template
    return render(request, 'courses/course_lessons.html', {
        'course': course,
        'lessons': lessons
    })


@login_required
def lesson_detail(request, lesson_id):
    # Fetch the lesson object by its ID
    lesson = get_object_or_404(Lesson, id=lesson_id)

    # Pass the lesson to the template
    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson
    })



# View for displaying all assignments associated with a lesson
@login_required
def view_assignments(request, lesson_id):
    # Fetch the lesson object and its associated assignments
    lesson = get_object_or_404(Lesson, id=lesson_id)
    assignments = Assignment.objects.filter(lesson=lesson)

    # Pass lesson and assignments to the template for rendering
    return render(request, 'assignments/view_assignments.html', {
        'lesson': lesson,
        'assignments': assignments
    })

# View for handling assignment submissions by the student
@login_required
def submit_assignment(request, assignment_id):
    # Fetch the assignment object by its ID or return a 404 error if not found
    assignment = get_object_or_404(Assignment, id=assignment_id)

    # If the method is POST, handle the assignment submission
    if request.method == "POST":
        content = request.POST.get("content")  # Get the assignment content from the form
        file = request.FILES.get("file")  # Get the file uploaded by the student

        # Create a new Submission object for this assignment
        submission = Submission.objects.create(
            assignment=assignment,
            student=request.user,
            content=content,
            file=file,
        )

        # Optionally, redirect to a submission confirmation page
        return redirect('assignment_submitted')

    # If the request is not POST, render the submission form for the assignment
    return render(request, 'assignments/submit_assignment.html', {'assignment': assignment})

# View for displaying all quizzes associated with a lesson
@login_required
def view_quiz(request, lesson_id):
    # Fetch the lesson object and its associated quizzes
    lesson = get_object_or_404(Lesson, id=lesson_id)
    quizzes = Quiz.objects.filter(lesson=lesson)

    # Pass lesson and quizzes to the template for rendering
    return render(request, 'quizzes/view_quizzes.html', {
        'lesson': lesson,
        'quizzes': quizzes
    })

# View for completing a quiz, including submitting answers and displaying results
@login_required
def complete_quiz(request, quiz_id):
    # Fetch the quiz object by its ID and get the associated questions
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    # If the request is POST, handle the quiz submission
    if request.method == "POST":
        score = 0
        # Check each answer and calculate the score
        for question in questions:
            selected_answer = request.POST.get(f"question_{question.id}")
            if selected_answer == question.correct_answer:
                score += 1

        # Optionally, you can create a record for the quiz submission here
        # and store the score for future grading or statistics
        return render(request, 'quizzes/quiz_results.html', {'score': score, 'total_marks': quiz.total_marks})

    # If the request is not POST, render the quiz page with the questions
    return render(request, 'quizzes/complete_quiz.html', {'quiz': quiz, 'questions': questions})


# View to display all courses the student is currently enrolled in
@login_required
def enrolled_courses(request):
    # Fetch all enrollments for the current student (logged-in user)
    enrolled_courses = Enrollment.objects.filter(student=request.user)

    # Pass the enrolled courses to the template for rendering
    return render(request, 'courses/enrolled_courses.html', {'enrolled_courses': enrolled_courses})
