import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey

from .choices import SEMESTER_CHOICES, EXAM_CHOICES


def filePath(instance, filename):
    filename = f"{instance.subject}_{instance.year}_{instance.semester}_{instance.exam}.pdf"
    return f'files/{filename}'


class Branch(models.Model):
    name = models.CharField(unique=True, max_length=256)

    def __str__(self):
        return self.name


class Subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject_code = models.CharField(unique=True, max_length=10)
    subject_name = models.CharField(unique=True, max_length=256)
    subject_name_short = models.CharField(unique=True, max_length=5)

    def __str__(self):
        return self.subject_name


class QuestionPaper(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    subject = ChainedForeignKey(
        Subject,
        on_delete=models.CASCADE,
        chained_field="branch",
        chained_model_field="branch",
    )
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(datetime.date.today().year),
        ],
        help_text="Please use the following format: <em>YYYY</em>.",
    )
    semester = models.CharField(
        max_length=4,
        choices=SEMESTER_CHOICES,
        default='ODD',
    )
    exam = models.CharField(
        max_length=7,
        choices=EXAM_CHOICES,
        default='MST-1',
    )

    paper = models.FileField(
        upload_to=filePath,
        null=True,
        validators=[
            FileExtensionValidator(['pdf'])
        ],
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.paper.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.subject}_{self.year}_{self.semester}_{self.exam}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['subject', 'year', 'semester', 'exam'],
                name='unique paper'
            ),
        ]
