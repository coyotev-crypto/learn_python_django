from django.db import models


class Course(models.Model):
    '''课程表映射类，包括课程名字、发布时间和学习人数等属性
    '''

    name = models.CharField(max_length=64)
    pub_date = models.DateField()
    stu_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Author(models.Model):
    '''课程作者映射类，包括作者名字、性别等属性
    '''

    name = models.CharField(max_length=64)
    gender = models.BooleanField(null=True)

    def __str__(self):
        return self.name
