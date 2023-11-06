
class BatteryFactory:
    @staticmethod
    def create_battery(last_service_date, capacity):
        return Battery(last_service_date, capacity)

if car_part_type == [CarPartType]:
    return [CarPart]Factory.create_car_part(last_service_date, additional_attributes)

def needs_service(self) -> bool:
    for service_criteria_strategy in self.service_criteria_strategies:
        if service_criteria_strategy.needs_service(self):
            return True

    return False

class [ServiceCriteria]Strategy(ServiceCriteriaStrategy):
    def __init__(self, additional_attributes):
        self.additional_attributes = additional_attributes

    def needs_service(self, car_part: [CarPart]) -> bool:
        # Implement the service criteria logic here
        pass

class [ServiceCriteria]Strategy:
    @abstractmethod
    def needs_service(self, car_part: [CarPart]) -> bool:
        pass


class BatteryCapacityServiceCriteria(ServiceCriteriaStrategy):
    def __init__(self, capacity_threshold):
        self.capacity_threshold = capacity_threshold

    def needs_service(self, battery: Battery) -> bool:
        return battery.capacity < self.capacity_threshold


class LowBatteryCapacityServiceCriteria(BatteryCapacityServiceCriteria):
    def __init__(self):
        super().__init__(50)
