from django.core.management.base import BaseCommand
from main.management.base_load_data import DummyData
import sys


class Command(BaseCommand):
    help = 'main script'

    def run(self, cls):
        try:
            cls.perform()
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print('Exception..')
        del cls

    def handle(self, *args, **options):
        dummy = DummyData()
        self.run(dummy)
