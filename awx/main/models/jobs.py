# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

# Python
import logging
import time
from urllib.parse import urljoin


# Django
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Cast

# AWX

from awx.main.models.base import (
    BaseModel,
    CreatedModifiedModel,
    accepts_json,
    JOB_TYPE_CHOICES,
    NEW_JOB_TYPE_CHOICES,
    VERBOSITY_CHOICES,
    VarsDictProperty,
)

from awx.main.models.unified_jobs import UnifiedJobTemplate, UnifiedJob

logger = logging.getLogger('awx.main.models.jobs')

class JobOptions(BaseModel):
    """
    Common options for job templates and jobs.
    """

    class Meta:
        abstract = True

    
class Job(UnifiedJob, JobOptions):
    """
    """

    class Meta:
        app_label = 'main'
        ordering = ('id',)

    