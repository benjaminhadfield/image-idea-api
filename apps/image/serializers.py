from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    source = serializers.ImageField(use_url=False)

    class Meta:
        model = Image
        fields = '__all__'
