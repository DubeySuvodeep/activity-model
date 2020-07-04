from django.core.management.base import BaseCommand, CommandError
from activity_model.models import User, ActivityPeriod
from django.utils import timezone

dummy = {
    'members' : [
            {
                "name":"ABC1", 
                "location":"Bangalore",
                "activity_periods" : [
                    {"start_time": "2020-07-04T12:49:00Z",
                    "end_time": "2020-07-04T12:49:07Z"}
                ]
            },
        ],
} 


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(dummy)
        for i in dummy['members']:
            u = User.objects.create(name=i['name'], location=i['location'])
            ActivityPeriod(user=u, 
                            start_time=i['activity_periods'][0]['start_time'], 
                            end_time=i['activity_periods'][0]['end_time']
                        )