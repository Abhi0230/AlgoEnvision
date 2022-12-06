# Generated by Django 3.2.13 on 2022-04-29 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First Name', max_length=33)),
                ('last_name', models.CharField(help_text='Last Name', max_length=33)),
                ('email', models.EmailField(max_length=33, unique=True)),
                ('mobile', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=33)),
                ('subject', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Data Science', 'Data Science')], max_length=15)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='AssignmentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=33)),
                ('subject', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=55)),
                ('document', models.FileField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherApp.teachermodel')),
            ],
            options={
                'db_table': 'Assignments',
            },
        ),
    ]