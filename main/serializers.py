from rest_framework import serializers
from main.models import Member, Activity_Period

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity_Period
        fields = ['start_time', 'end_time']

class MemberSerializer(serializers.ModelSerializer):
    activity = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_activity(self, obj):
        activities = obj.activity_period_set.all()
        if activities:
            serialized_activies = ActivitySerializer(activities, many=True)
            return serialized_activies.data
        return None
