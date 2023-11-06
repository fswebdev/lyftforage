from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date, service_criteria_strategies):
        self.last_service_date = last_service_date
        self.service_criteria_strategies = service_criteria_strategies

    def needs_service(self) -> bool:
        for service_criteria_strategy in self.service_criteria_strategies:
            if service_criteria_strategy.needs_service(self):
                return True

        return False

class CarFactory:
    @staticmethod
    def create_car(last_service_date, car_type, additional_attributes):
        if car_type == CarType.BATTERY:
            return BatteryFactory.create_battery(last_service_date, additional_attributes['capacity'])

class [CarPart]Factory:
    @staticmethod
    def create_car_part(last_service_date, additional_attributes):
        return [CarPart](last_service_date, additional_attributes)
