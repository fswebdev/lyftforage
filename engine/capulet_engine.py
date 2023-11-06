from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    __factory = CapuletEngineFactory

    @classmethod
    def create(cls, last_service_date, current_mileage, last_service_mileage):
        return cls.__factory.create_engine(last_service_date, current_mileage, last_service_mileage)

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, MileageServiceCriteria())

    def engine_should_be_serviced(self):
       return self.current_mileage - self.last_service_mileage > 30000
       
class CapuletEngineFactory:
    @staticmethod
    def create_engine(last_service_date, current_mileage, last_service_mileage):
        return CapuletEngine(last_service_date, current_mileage, last_service_mileage)
