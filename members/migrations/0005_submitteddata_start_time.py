# Generated by Django 4.2.6 on 2024-02-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_submitteddata_candidate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitteddata',
            name='start_time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
