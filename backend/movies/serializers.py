from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'description', 'url')
        read_only_fields = ('title', 'year', 'description', 'url')
