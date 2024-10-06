
from awx.main import models

from awx.api import serializers

# AWX
from awx.api.generics import (
    ListCreateAPIView
)

class ProjectList(ListCreateAPIView):
    model = models.Project
    serializer_class = serializers.ProjectSerializer