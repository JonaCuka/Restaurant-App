import unittest
from order_calculator import AbstractOrderCalculator
from base_model import Menu, OrderItems
from base_enums import  OrderItemSize

class OrderCalculatorMock(AbstractOrderCalculator):
    def _get_vat_rate(self):
        return 0.12

    def _get_size_rate_amount(self, order_item_size):
        return 1.1   
#mock class for tsting
class AbstractOrderCalculatorTest(unittest.TestCase):
    #create setup method to prepare test method
    #the method set up will be executed beefore each test method
    def setUp(self):
        self.order_calculator_mock = OrderCalculatorMock()

class OrderCalculatorMock(AbstractOrderCalculator):
    def _get_vat_rate(self):
        return 0.12

    def _get_size_rate_amount(self, order_item_size):
        return 1.1   
#mock class for tsting
class AbstractOrderCalculatorTest(unittest.TestCase):
    #create setup method to prepare test method
    #the method set up will be executed beefore each test method
    def setUp(self):
        self.order_calculator_mock = OrderCalculatorMock()   
        self.menu = Menu()

    def test_calculate_order_item_price(self):

        hamburger = self.menu.get_menu_items().get(100)
        order_item = OrderItems(hamburger, OrderItemSize.MEDIUM, 2)

    #CALCULATE METHOD THAT SHOULD BE TESTED ON TEST OBJECT
        total_order_item_price  = self.order_calculator_mock.calculate_order_item_price(order_item)

        self.assertEqual(9.9, total_order_item_price)
        self.assertEqual(4.5, order_item.get_order_item_price) 
       