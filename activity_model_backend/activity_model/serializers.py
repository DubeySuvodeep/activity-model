import os

from django.conf import settings
from rest_framework import serializers

from activity_model.models import User, ActivityPeriod


class ReadActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = '__all__'


class ReadUserSerializer(serializers.ModelSerializer):

    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_activity_periods(self, obj):
        activity_periods = ActivityPeriod.objects.filter(user__id=obj.id)
        serializer = ReadActivitySerializer(activity_periods, many=True)
        return serializer.data


# class ReadResponseSerializer(serializers.Serializer):

#     members = ReadUserSerializer(many=True)    