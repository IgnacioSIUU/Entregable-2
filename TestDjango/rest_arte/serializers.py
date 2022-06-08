from rest_framework import serializers
from core.models import Arte
class ArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arte
        fields =['idprod','nombre','precio', 'categoria']