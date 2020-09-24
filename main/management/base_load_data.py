import uuid
import random
import datetime
import dateutil
from dateutil.relativedelta import relativedelta
from main.models import Member, Activity_Period
from main.utils import timezones, random_names

class DummyData:

    def perform(self):
        print("We are Ready For Dummy Data")
        activity_records = 50
        member_recoords = 10
        start = datetime.datetime.now(tz=datetime.timezone.utc)
        end = start + relativedelta(months=4)
        dates = []
        members = []

        while member_recoords:
            member  =Member.objects.create(id=str(uuid.uuid4()), real_name=random.choice(random_names), tz=random.choice(timezones))
            members.append(member)
            member_recoords = member_recoords -1
        print("Members Are Created")

        while len(dates) !=activity_records:
            ran = random.randint(1,59)
            date = (start + relativedelta(days=ran), end - relativedelta(days=ran))
            if date not in dates:
                activity = Activity_Period.objects.create(start_time=date[0], end_time=date[-1], member=random.choice(members))
                dates.append(date)
        print("Activities Are Created")
