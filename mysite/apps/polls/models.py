from email.policy import default
from typing_extensions import Self
from django.db import models
import sqlite3

class SubejctManager(models.Manager):
    def GetTime(self):
        return self.annotate()


class Subject(models.Model):
    name = models.CharField("Название дисциплины", max_length = 130)
    lecture_practice = models.CharField("Тип", max_length = 4, default = '')

    def __str__(self):
        return  f"""{self.name}, ({self.lecture_practice})"""

    def obj(self):
        return f"""{self.name}"""

    def getname(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
    
    def get_absolute_url(self):
        return f'/polls/{self.id}/'

    def __eq__(self, obj: Self) -> bool:
        return self.name == obj.name and self.lecture_practice == obj.lecture_practice

    # SubManager = SubjectManager()

class Timetable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.CharField('Время', max_length = 40)
    room = models.CharField('Аудитория', max_length = 10)
    weekday = models.CharField('День', max_length = 30)

    def __str__(self):
        return f"""poll: {self.subject} | {self.time} | {self.room}"""

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

