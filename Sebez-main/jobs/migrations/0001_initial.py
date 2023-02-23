# Generated by Django 4.0.4 on 2022-04-25 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('source_link', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('job_type', models.SmallIntegerField(choices=[(1, 'Full Time'), (2, 'Contract'), (3, 'Part Time')], default=1)),
                ('status', models.SmallIntegerField(choices=[(0, 'Save Draft'), (1, 'Publish Now')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='jobs.jobcategory')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='accounts.employer')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]