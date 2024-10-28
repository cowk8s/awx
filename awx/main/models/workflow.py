# Copyright (c) 2016 Ansible, Inc.
# All Rights Reserved.

# Python
import json
import logging
from uuid import uuid4
from copy import copy
from urllib.parse import urljoin

from awx.main.models.base import CreatedModifiedModel, VarsDictProperty

from awx.main.models.jobs import LaunchTimeConfigBase, LaunchTimeConfig, JobTemplate

__all__ = [

]

logger = logging.getLogger('awx.main.models.workflow')

WORKFLOW_BASE_URL = "{}/jobs/workflow/{}"


class WorkflowNodeBase(CreatedModifiedModel, LaunchTimeConfig):
    class Meta:
        abstract = True
        app_label = 'main'