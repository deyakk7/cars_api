from django.core.management import BaseCommand

from car.utils import CarGenerator


class Command(BaseCommand):

    help = "Generates records into db from third party api"

    def add_arguments(self, parser):
        parser.add_argument("count", action="store", nargs="+", type=int)

    def handle(self, *args, **options):

        count = options["count"][0]
        car_generator = CarGenerator()

        car_generator.fetch_cars(count)

        return self.stdout.write("completed")
