# Generated by Django 4.2.9 on 2024-07-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_results_no_of_questions_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='no_of_questions_attended',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
