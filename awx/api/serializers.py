
# AWS

from awx.main.models import (
    Project
)

class ProjectSerializer():

    class Meta:
        model = Project
        fields = (
            '*',
            'organization'
        )
        read_only_fields = ('*', 'custom_virtualenv')