# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


    CURRENCY_CHOICES = (
        ('EUR', '€'),
        ('DOL', '$'),
        ('LIR', '£'),
        ('YEN', '¥')
    )
    PROJECT_STATE = (
        ('0', _(u'Draft')),
        ('1', _(u'Quotation')),
        ('2', _(u'Bill')),
        ('3', _(u'Refused'))
    )

class Project(models.Model):
    title = models.CharField(_(u'Task name'), max_length=255)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    default_unit_rate = models.IntegerField(_(u'Default unit rate'))
    state = models.IntegerField(_(u'Project status'), choices=PROJECT_STATE)
    default_currency = models.CharField(_(u'Currency'), max_length=5, choices=CURRENCY_CHOICES)

    def __unicode__(self):
        return u'%s' % (self.title)



class Task(models.Model):
    title = models.CharField(_(u'Task name'), max_length=255)
    number_of_units = models.IntegerField(_(u'Hour'))
    unit_rate = models.IntegerField(_(u'Rate'))
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return u'%s' % (self.title)
