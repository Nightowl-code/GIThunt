# Generated by Django 4.2.6 on 2024-02-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_submitteddata_q'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitteddata',
            name='qno',
        ),
        migrations.RemoveField(
            model_name='submitteddata',
            name='text_data',
        ),
        migrations.AddField(
            model_name='submitteddata',
            name='candidate',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='submitteddata',
            name='list',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='submitteddata',
            name='time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
