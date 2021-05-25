# Generated by Django 3.2.3 on 2021-05-25 05:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import questions.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=10, unique=True)),
                ('subject_name', models.CharField(max_length=256, unique=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.branch')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(help_text='Please use the following format: <em>YYYY</em>.', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2021)])),
                ('semester', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], default='ODD', max_length=4)),
                ('exam', models.CharField(choices=[('MST-1', 'Midsemester Examination 1'), ('MST-2', 'Midsemester Examination 2'), ('END-SEM', 'Endsemester Examination')], default='MST-1', max_length=7)),
                ('paper', models.FileField(null=True, upload_to=questions.models.filePath, validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.branch')),
                ('subject', smart_selects.db_fields.ChainedForeignKey(chained_field='branch', chained_model_field='branch', on_delete=django.db.models.deletion.CASCADE, to='questions.subject')),
            ],
        ),
        migrations.AddConstraint(
            model_name='questionpaper',
            constraint=models.UniqueConstraint(fields=('subject', 'year', 'semester', 'exam'), name='unique paper'),
        ),
    ]
