from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CustomCourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class CustomLessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class CustomQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Course, CustomCourseAdmin)
admin.site.register(Lesson, CustomLessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, CustomQuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)