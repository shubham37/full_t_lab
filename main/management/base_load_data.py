import logging
import uuid
import random
import datetime
import dateutil
from dateutil.relativedelta import relativedelta
from main.models import Member, Activity_Period
from main.utils import timezones, random_names

logger = logging.getLogger(__name__)


class DummyData:

    def __init__(self, members_num):
        self.members_num = members_num

    def perform(self):
        member_records = self.members_num
        activity_records = member_records*5
        start = datetime.datetime.now(tz=datetime.timezone.utc)
        end = start + relativedelta(months=4)
        dates = []
        members = []
        while member_records:
            member  =Member.objects.create(id=str(uuid.uuid4()), real_name=random.choice(random_names), tz=random.choice(timezones))
            members.append(member)
            member_records = member_records -1
        logger.info("%s Members Are Created", len(members))

        while len(dates) !=activity_records:
            ran = random.randint(1,59)
            date = (start + relativedelta(days=ran), end - relativedelta(days=ran))
            if date not in dates:
                activity = Activity_Period.objects.create(start_time=date[0], end_time=date[-1], member=random.choice(members))
                dates.append(date)
        logger.info("%s Members Are Created", len(dates))
