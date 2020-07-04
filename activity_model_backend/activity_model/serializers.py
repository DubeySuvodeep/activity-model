import os
import datetime

from django.conf import settings
from rest_framework import serializers

from activity_model.models import User, ActivityPeriod


class ReadActivitySerializer(serializers.ModelSerializer):

    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

    def get_start_time(self, obj):
        time = obj.start_time.strftime('%b %d, %Y %I:%M %p')
        return time

    def get_end_time(self, obj):
        time = obj.start_time.strftime('%b %d, %Y %I:%M %p')
        return time


class ReadUserSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()
    tz = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

    def get_id(self, obj):
        return obj.id

    def get_real_name(self, obj):
        return obj.name

    def get_tz(self, obj):
        return obj.location

    def get_activity_periods(self, obj):
        activity_periods = ActivityPeriod.objects.filter(user__id=obj.id)
        serializer = ReadActivitySerializer(activity_periods, many=True)
        return serializer.data
