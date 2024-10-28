
from awx.main import models

from awx.api import serializers

# AWX
from awx.api.generics import (
    ListCreateAPIView,
    RetrieveAPIView
)

class ProjectList(ListCreateAPIView):
    model = models.Project
    serializer_class = serializers.ProjectSerializer

class AdHocCommandEventDetail(RetrieveAPIView):
    model = models.AdHocCommandEvent
    serializer_class = serializers.AdHocCommandEventSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(no_truncate=True)
        return context