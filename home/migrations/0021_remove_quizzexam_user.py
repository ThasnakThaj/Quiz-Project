# Generated by Django 4.2.9 on 2024-08-11 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_questions_medium"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quizzexam",
            name="user",
        ),
    ]