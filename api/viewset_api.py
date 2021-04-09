from .models import Kelompok
from .serializers import KelompokSelializers
from rest_framework import viewsets, permissions

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSelializers
    # permission_classes = [permissions.IsAuthenticated]
    # allow type protocol api
    http_method_names = ['put'] 