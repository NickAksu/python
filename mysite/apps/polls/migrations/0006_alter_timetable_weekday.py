# Generated by Django 4.2.dev20220827135108 on 2022-10-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0005_timetable_weekday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timetable",
            name="weekday",
            field=models.CharField(max_length=10, verbose_name="День"),
        ),
    ]
