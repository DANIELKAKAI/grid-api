from rest_framework import serializers

from main.models import Grid


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ('points', 'closest_points')

    points = serializers.CharField(write_only=True)
    closest_points = serializers.CharField(read_only=True)
