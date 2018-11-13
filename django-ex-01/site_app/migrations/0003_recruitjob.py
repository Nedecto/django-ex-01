# Generated by Django 2.1.2 on 2018-11-12 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.Job')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.Recruit')),
            ],
        ),
    ]
