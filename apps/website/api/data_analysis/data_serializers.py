from rest_framework import serializers
from apps.website.models import Dataframe

class DataframeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataframe
        fields = '__all__'
