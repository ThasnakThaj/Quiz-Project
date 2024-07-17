# Generated by Django 4.2.9 on 2024-07-15 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.questions'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.choices'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.questions'),
        ),
        migrations.CreateModel(
            name='QuizzExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_phone', models.BigIntegerField()),
                ('question_id', models.IntegerField()),
                ('question_name', models.CharField(max_length=250)),
                ('selected_choice', models.CharField(max_length=200)),
                ('correct_choice', models.CharField(max_length=200)),
                ('is_answer_correct', models.BooleanField(default=False)),
                ('choice_selected_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
