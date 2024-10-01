from random import shuffle, choice

import requests as rq
from faker import Faker
from faker_vehicle import VehicleProvider

from brand.models import Brand
from car.models import Car
from model.models import Model


class CarGenerator:
    def __init__(self):
        self.fake = Faker()
        self.fake.add_provider(VehicleProvider)

        self.URL = "https://freetestapi.com/api/v1/cars"
        self.fuel_types = {
            "Gasoline": "gasoline",
            "Diesel": "diesel",
            "Electric": "electric",
            "Hybrid": "hybrid",
        }

        self.transmission_types = {
            "Manual": "manual",
            "Automatic": "automatic",
        }

    def create_car(self, count: int = 1):
        for _ in range(count):
            brand_obj, created = Brand.objects.get_or_create(
                name=self.fake.vehicle_make(), defaults={"country": self.fake.country()}
            )

            model_obj, created = Model.objects.get_or_create(
                name=self.fake.vehicle_model(),
                year=self.fake.random_int(min=1900, max=2024),
                body_type=self.fake.random_element(
                    elements=(
                        "sedan",
                        "hatchback",
                        "liftback",
                        "coupe",
                        "crossover",
                        "truck",
                        "wagon",
                    )
                ),
            )

            Car.objects.create(
                brand=brand_obj,
                model=model_obj,
                price=self.fake.random_number(digits=6),
                mileage=self.fake.random_number(digits=7),
                exterior_color=self.fake.color_name(),
                interior_color=self.fake.color_name(),
                fuel_type=self.fake.random_element(
                    elements=("gasoline", "diesel", "electric", "hybrid")
                ),
                transmission=self.fake.random_element(elements=("manual", "automatic")),
                engine=self.fake.random_element(
                    elements=("2.0L", "1.6L", "3.0L", "4.4L")
                ),
                on_sale=bool(choice([0, 1])),
            )

    def fetch_cars(self, count: int = 1):

        response = rq.request(
            method="GET",
            url=self.URL,
        )

        response_data = response.json()
        shuffle(response_data)

        for car in response_data[:count]:
            brand_name = car["make"]
            model_name = car["model"]
            year = car["year"]
            fuel_type = car["fuelType"]
            transmission = car["transmission"]
            engine = car["engine"]
            price = car["price"]
            mileage = car["mileage"]
            exterior_color = interior_color = car["color"]

            brand_obj, created = Brand.objects.get_or_create(
                name=brand_name, defaults={"country": self.fake.country()}
            )

            model_obj, created = Model.objects.get_or_create(
                name=model_name,
                year=year,
                body_type=self.fake.random_element(
                    elements=(
                        "sedan",
                        "hatchback",
                        "liftback",
                        "coupe",
                        "crossover",
                        "truck",
                        "wagon",
                    )
                ),
            )

            Car.objects.create(
                brand=brand_obj,
                model=model_obj,
                price=price,
                mileage=mileage,
                exterior_color=exterior_color,
                interior_color=interior_color,
                fuel_type=self.fuel_types.get(fuel_type, "Gasoline"),
                transmission=self.transmission_types.get(transmission, "Automatic"),
                engine=engine,
                on_sale=bool(self.fake.boolean(chance_of_getting_true=50)),
            )


# {
#       "id": 24,
#     "make": "Toyota",
#     "model": "Highlander",
#     "year": 2020,
#     "color": "Silver",
#     "mileage": 20000,
#     "price": 36000,
#     "fuelType": "Gasoline",
#     "transmission": "Automatic",
#     "engine": "3.5L V6",
#     "horsepower": 295,
#     "features": [
#       "Lane Departure Alert",
#       "Third-Row Seating",
#       "Smart Key System"
#     ],
#     "owners": 2,
#     "image": "https://fakeimg.pl/500x500/cccccc"
# }
