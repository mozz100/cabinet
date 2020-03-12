from .models import Trophy
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class TrophySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trophy
        fields = ('name', 'weight')

# ViewSets define the view behavior.
class TrophyViewSet(viewsets.ModelViewSet):
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer
