# Generated by Django 4.0.4 on 2022-06-09 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_jobseeker_resume_alter_jobseeker_user'),
        ('jobs', '0004_jobapplication_resume_alter_job_deadline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.SmallIntegerField(choices=[(1, 'It is offensive, descriminatory'), (2, 'It seems like a fake job'), (3, 'Vague description'), (4, 'Other')])),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Addtional information')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddConstraint(
            model_name='jobapplication',
            constraint=models.UniqueConstraint(fields=('job', 'jobseeker'), name='unique_application'),
        ),
        migrations.AddField(
            model_name='report',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reports', to='jobs.job'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reports', to='accounts.jobseeker'),
        ),
        migrations.AddConstraint(
            model_name='report',
            constraint=models.UniqueConstraint(fields=('job', 'user'), name='unique_report'),
        ),
    ]