# Generated by Django 4.2.dev20220827135108 on 2022-10-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_subject_timetable_delete_comment_delete_poll"),
    ]

    operations = [
        migrations.AddField(
            model_name="timetable",
            name="weekday",
            field=models.CharField(default="", max_length=10, verbose_name="День"),
        ),
    ]