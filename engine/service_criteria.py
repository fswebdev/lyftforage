class ServiceCriteria:
    @abstractmethod
    def needs_service(self, engine: Car) -> bool:
        pass

class MileageServiceCriteria(ServiceCriteria):
    def needs_service(self, engine: Car) -> bool:
        return engine.current_mileage - engine.last_service_mileage > 30000

class WarningLightServiceCriteria(ServiceCriteria):
    def needs_service(self, engine: Car) -> bool:
        return engine.warning_light_is_on

class CombinedServiceCriteria(ServiceCriteria):
    def __init__(self, service_criterias: List[ServiceCriteria]):
        self.service_criterias = service_criterias

    def needs_service(self, engine: Car) -> bool:
        for service_criteria in self.service_criterias:
            if service_criteria.needs_service(engine):
                return True

        return False