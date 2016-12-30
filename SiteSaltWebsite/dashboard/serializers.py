from dashboard.models import Dinosaur
from rest_framework import serializers


class DinosaurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ('url', 'species')
