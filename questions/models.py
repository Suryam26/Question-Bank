import uuid
import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.contrib.postgres.search import SearchVectorField
from smart_selects.db_fields import ChainedForeignKey

from .choices import SEMESTER_CHOICES
from .model_manager import QuestionPaperManager, filePath


class Branch(models.Model):
    name = models.CharField(unique=True, max_length=256)

    def __str__(self):
        return self.name


class Subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject_code = models.CharField(unique=True, max_length=10)
    subject_name = models.CharField(max_length=256)
    subject_name_short = models.CharField(max_length=5)

    def __str__(self):
        return self.subject_name


class Exam(models.Model):
    name = models.CharField(max_length=7)
    name_1 = models.CharField(max_length=7)
    name_2 = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class QuestionPaper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

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
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

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

    search_vector = SearchVectorField(null=True)

    objects = QuestionPaperManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if ("update_fields" not in kwargs or "search_vector" not in kwargs["update_fields"]):
            instance = (
                self._meta.default_manager.with_documents().get(pk=self.pk))
            instance.search_vector = instance.document
            instance.save(update_fields=["search_vector"])

    def delete(self, *args, **kwargs):
        self.paper.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.subject}_{self.year}_{self.semester}_{self.exam}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.uploaded_at <= now

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['branch', 'subject', 'year', 'semester', 'exam'],
                name='unique paper'
            ),
        ]
