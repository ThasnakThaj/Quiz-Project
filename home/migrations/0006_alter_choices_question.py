# Generated by Django 4.2.9 on 2024-07-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_choices_question_alter_exam_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='home.questions'),
        ),
    ]