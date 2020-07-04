from django.core.management.base import BaseCommand, CommandError
from activity_model.models import User, ActivityPeriod
from django.utils import timezone

dummy = {
    'members' : [
            {
                "name":"Sanjeev", 
                "location":"Bangalore",
                "activity_periods" : [
                    {"start_time": "2020-07-04T12:49:00Z",
                    "end_time": "2020-07-04T12:49:07Z"}
                ]
            },
            {
                "name":"Sachin", 
                "location":"Bangalore",
                "activity_periods" : [
                    {"start_time": "2020-07-04T12:49:00Z",
                    "end_time": "2020-07-04T12:49:07Z"},
                    {"start_time": "2020-07-04T12:54:00Z",
                    "end_time": "2020-07-04T12:57:07Z"}
                ]
            },
        ],
} 


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(dummy)
        for i in dummy['members']:
            try:
                u = User.objects.create(name=i['name'], location=i['location'])
                for j in i['activity_periods']:
                    try:
                        ActivityPeriod.objects.create(user=u, 
                                        start_time=j['start_time'], 
                                        end_time=j['end_time']
                                        )
                    except Exception as e:
                        print(e)        
            except Exception as e:
                print(e)