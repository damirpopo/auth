from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50,verbose_name='Предмет')

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст')
    subjects = models.ForeignKey('Subject', on_delete=models.CASCADE,verbose_name='Предмет')

    def __str__(self):
        return self.full_name


class Class(models.Model):
    class_name = models.CharField(max_length=4)
    year = models.IntegerField(verbose_name='Год обучения')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    CHOICES = [
        (5, 'Отлично'),
        (4, 'Хорошо'),
        (3, 'Удовлетворительно'),
        (2, 'Неудовлетворительно'),
    ]
    grade = models.IntegerField(choices=CHOICES,verbose_name='Оценки',null=True)
