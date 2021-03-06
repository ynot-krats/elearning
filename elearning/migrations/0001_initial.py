# Generated by Django 3.0.7 on 2020-06-30 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(default='', max_length=150)),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='elearning.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(default='', max_length=200)),
                ('lessonText', models.CharField(default='', max_length=1000)),
                ('videolink', models.CharField(default='', max_length=500)),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='elearning.Courses')),
                ('section', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='elearning.Section')),
            ],
        ),
    ]
