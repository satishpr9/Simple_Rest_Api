from rest_framework import serializers

from .models import Api

class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Api
        fields=('image','img1','img2','img3','img4','img5','img6' )