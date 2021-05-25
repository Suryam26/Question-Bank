from django.contrib import admin

from .models import QuestionPaper, Branch, Subject


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'subject_code', 'branch', ]


class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ['subject', 'exam', 'year', 'semester', ]


admin.site.register(Branch, BranchAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(QuestionPaper, QuestionPaperAdmin)
