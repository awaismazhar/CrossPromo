from rest_framework import serializers
from .models import *

class AdvertismentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model=AdvertismentInfo
        fields='__all__'