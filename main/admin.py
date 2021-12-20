from django.contrib import admin
from .models import Question,Answer,Points


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'point']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Points)
