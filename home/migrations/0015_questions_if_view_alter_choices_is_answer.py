# Generated by Django 4.2.9 on 2024-07-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_results_ip_address_user_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='if_view',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='choices',
            name='is_answer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
