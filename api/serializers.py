from .models import Kelompok
from rest_framework import serializers

class KelompokSelializers(serializers.ModelSerializer):
    class Meta:
        model = Kelompok
        fields = ['id', 'nama', 'keterangan']
        