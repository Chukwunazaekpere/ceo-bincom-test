from rest_framework import viewsets

from .models import (
    Voters
)
from .serializers import (
    VotersSerializer
)


class VotersViewSet(viewsets.ModelViewSet):
    queryset = Voters.objects.all()
    serializer_class = VotersSerializer

    
