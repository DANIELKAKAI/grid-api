from rest_framework import serializers

from main.models import Grid


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ('id', 'points', 'closest_points')
        read_only_fields = ('closest_points',)
