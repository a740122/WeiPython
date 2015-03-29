from django.db import models


class Student(models.Model):
    """Student Info"""
    stu_id = models.CharField('学号', max_length=30, primary_key=True)
    name = models.CharField('姓名', max_length=30)
    password = models.CharField('密码', max_length=30)

    def __unicode__(self):
        return '{stu_id} {name}'.format(stu_id=self.stu_id, name=self.name)


class Teacher(models.Model):
    """Teacher Info"""
    name = models.CharField('姓名', max_length=30)

    def __unicode__(self):
        return self.name


class Questoin(models.Model):
    """Question Info"""
    title = models.TextField()
    content = models.TextField()
    answer = models.CharField(max_length=1)

    def __unicode__(self):
        return self.title


class Notification(self):
    """Notification Info"""
    title = models.TextField()
    content = models.TextField()
    time = models.DateField()

    def __unicode__(self):
        return self.title
