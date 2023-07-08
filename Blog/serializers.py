from rest_framework import serializers

from Blog.models import *

class ShoeMS(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'
        