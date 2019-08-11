# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Students(models.Model):
    roll_no = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=200, null=False)
    branch = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=12, null=False)
    city = models.CharField(max_length=1024, null=False)

class Teacher(models.Model):
    tid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=12, null=False)

class Subject(models.Model):
    name = models.CharField(max_length=100,null=False)
    sub_code = models.CharField(max_length=100,null=False)
    questions = models.ManyToManyField('Questions')

class Answer(models.Model):
    string = models.CharField(max_length=1024)

class Questions(models.Model):
    string = models.CharField(max_length=1020)
    answer = models.ForeignKey(Answer, related_name="right_answer")
    options = models.ManyToManyField(Answer, related_name="Options_for_questions")

