# Generated by Django 4.2.9 on 2024-07-13 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='question',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]