# Generated by Django 4.2.6 on 2024-02-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_submitteddata_qno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitteddata',
            name='candidate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='submitteddata',
            name='list',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='submitteddata',
            name='time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
