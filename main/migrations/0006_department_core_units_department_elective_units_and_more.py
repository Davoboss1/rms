# Generated by Django 4.0.3 on 2022-08-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_course_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='core_units',
            field=models.SmallIntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='elective_units',
            field=models.SmallIntegerField(default=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='general_units',
            field=models.SmallIntegerField(default=30),
            preserve_default=False,
        ),
    ]
