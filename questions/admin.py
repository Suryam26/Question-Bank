from django.contrib import admin

from .models import QuestionPaper, Branch, Exam, Subject


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name',
                    'subject_name_short', 'subject_code', 'branch', ]


class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_1', 'name_2', ]


class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ['subject', 'exam', 'year', 'semester', ]


admin.site.register(Branch, BranchAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(QuestionPaper, QuestionPaperAdmin)
