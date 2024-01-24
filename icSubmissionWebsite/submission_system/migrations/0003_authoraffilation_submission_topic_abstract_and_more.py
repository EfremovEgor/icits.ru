# Generated by Django 5.0.1 on 2024-01-23 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission_system', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorAffilation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affilation', models.CharField(max_length=255, verbose_name='Affilation')),
                ('city', models.CharField(max_length=255, verbose_name='City/Suburb/Town')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Title')),
                ('presentation_type', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=300)),
                ('is_draft', models.BooleanField(default=True, verbose_name='Draft')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='submission_system.submission')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='submission_system.submission')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='submission_system.topic')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionAuthorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('organization', models.CharField(max_length=255, verbose_name='Last Name')),
                ('is_presenter', models.BooleanField(verbose_name='Presenter')),
                ('affilation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='submission_system.authoraffilation')),
                ('submission_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission_system.submissiondetails')),
            ],
        ),
    ]