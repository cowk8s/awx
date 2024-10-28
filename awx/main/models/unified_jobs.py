# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

# Python
from io import StringIO

from django.utils.translation import gettext_lazy as _

# Django-Polymorphic
from polymorphic.models import PolymorphicModel


__all__ = ['UnifiedJobTemplate', 'UnifiedJob', 'StdoutMaxBytesExceeded']

class UnifiedJobTemplate(PolymorphicModel):
    """
    Concrete base class for unified job templates.
    """

    # status inherits from related jobs. Thus, status must be able to be set to any status that a job status is settable to.
    JOB_STATUS_CHOICES = [
        ('new', _('New')),  # Job has been created, but not started.
        ('pending', _('Pending')),  # Job is pending Task Manager processing (blocked by dependency req, capacity or a concurrent job)
        ('waiting', _('Waiting')),  # Job has been assigned to run on a specific node (and is about to run).
        ('running', _('Running')),  # Job is currently running.
        ('successful', _('Successful')),  # Job completed successfully.
        ('failed', _('Failed')),  # Job completed, but with failures.
        ('error', _('Error')),  # The job was unable to run.
        ('canceled', _('Canceled')),  # The job was canceled before completion.
    ]

    COMMON_STATUS_CHOICES = JOB_STATUS_CHOICES + [
        ('never updated', _('Never Updated')),  # A job has never been run using this template.
    ]

    PROJECT_STATUS_CHOICES = COMMON_STATUS_CHOICES + [
        ('ok', _('OK')),  # Project is not configured for SCM and path exists.
        ('missing', _('Missing')),  # Project path does not exist.
    ]

    class Meta:
        app_label = 'main'
        ordering = ('name',)
        # unique_together here is intentionally commented out. Please make sure sub-classes of this model
        # contain at least this uniqueness restriction: SOFT_UNIQUE_TOGETHER = [('polymorphic_ctype', 'name')]
        # unique_together = [('polymorphic_ctype', 'name', 'organization')]

class UnifiedJob():
    """
    Concrete base class for unified job run by the task engine.
    """

    STATUS_CHOICES = UnifiedJobTemplate.JOB_STATUS_CHOICES

    PASSWORD_FIELDS = ('start_args',)

    class Meta:
        app_label = 'main'
        ordering = ('id',)

     