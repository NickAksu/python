# Generated by Django 4.2.dev20220827135108 on 2022-10-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0008_alter_timetable_room_alter_timetable_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="lecture_practice",
            field=models.CharField(default="", max_length=4, verbose_name="Тип"),
        ),
    ]