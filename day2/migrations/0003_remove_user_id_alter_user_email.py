# Generated by Django 5.0.2 on 2024-02-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day2', '0002_user_alter_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
