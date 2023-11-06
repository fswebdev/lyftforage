from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    __factory = CapuletEngineFactory

    @classmethod
    def create(last_service_date, warning_light_is_on):
        return cls.__factory.create_engine(last_service_date, warning_light_is_on)

    def __init__(last_service_date, warning_light_is_on):
        super().__init__(last_service_date,warning_light_is_on)

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
            
class SternmanEngineFactory:
    @staticmethod
    def create_engine(last_service_date, warning_light_is_on):
        return SternmanEngine(last_service_date, warning_light_is_on)

