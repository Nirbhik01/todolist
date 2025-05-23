# Generated by Django 5.1.6 on 2025-04-11 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=255)),
                ('task_description', models.TextField(blank=True, null=True)),
                ('task_status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='PENDING', max_length=15)),
                ('task_label', models.CharField(choices=[('WORK', 'Work'), ('GROCERY', 'Grocery'), ('STUDY', 'Study'), ('OTHER', 'Other')], default='WORK', max_length=10)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_task', models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.user')),
            ],
        ),
    ]
