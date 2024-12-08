from base_enums import Location
from order_calculator import OrderCalculatorGER, OrderCalculatorKS 

class OrderCalculatorFactory:
    @staticmethod
    def get_order_calculator_by_location(location):
        match(location):
            case Location.KOSOVO:
                return OrderCalculatorKS()
            case Location.GERMANY:
                return OrderCalculatorGER()
            case _:
                raise Exception("Current location is invalid. OrderCalculator could not be determined.")