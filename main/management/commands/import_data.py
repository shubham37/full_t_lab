import logging
from django.core.management.base import BaseCommand
from main.management.base_load_data import DummyData
import sys


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'main script'

    def add_arguments(self, parser):
        parser.add_argument('members_count', type=int)

    def run(self, cls):
        try:
            logger.info("We Are In Log")
            cls.perform()
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print('Exception..')
            logger.error(e)
        del cls

    def handle(self, *args, **options):
        logger.info("Dummy Data Insertion Start")
        dummy = DummyData(options['members'])
        self.run(dummy)
        logger.info("Dummy Data Insertion Start")
