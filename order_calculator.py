from abc import ABC, abstractmethod
from order_utils import OrderAmount , OrderItemSize
from custom_exeption import InvalidOrderItemSize


class AbstractOrderCalculator(ABC):

    def calculate_total_order_amount(self, order):
        order_items = order.get_product_list()  
        total_order_amount = 0.0
        
        for order_item in order_items:
            total_order_amount += self.calculate_order_item_price(order_item)  
        
        return total_order_amount
     

    def calculate_order_item_price(self, order_item):
        size_rate_amount = self.get_size_rate_amount(order_item.get_order_item_size())
        product = order_item.get_product()
        total_order_item_price_single = product.get_price() + size_rate_amount
        order_item.set_order_item_price(total_order_item_price_single)
        return total_order_item_price_single * order_item.get_quantity()

     
    def calculate_total_order_amount_vat(self, total_order_amount):
        return total_order_amount * self._get_vat_rate()
    
    def calculate_order_amount(self, order):
        total_order_amount = self.calculate_total_order_amount(order)
        total_order_amount_vat = self.calculate_total_order_amount_vat(total_order_amount)  
        total_order_amount_with_vat = total_order_amount + total_order_amount_vat

        order_amount = OrderAmount(total_order_amount, total_order_amount_vat, total_order_amount_with_vat)
        return order_amount
    

    
    #create abstract method 

    @abstractmethod
    def _get_vat_rate(self):
        pass

    def _get_size_rate_amount(self, order_item_size):
        pass


class OrderCalculatorKS(AbstractOrderCalculator):
    __VAT_RATE = 0.18

    

    def _get_vat_rate(self):
        return self.__VAT_RATE   

    def get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return  0.7
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.2
            #case OrderItemSize.XL:
                #return 1.4
            case OrderItemSize.XXL:
                return 1.25
            case _:
                raise InvalidOrderItemSize("This is not a valid order item size: " + order_item_size)
                #print("This is not a valid order item size: " + order_item_size)
        
        return 1 


class OrderCalculatorGER(AbstractOrderCalculator):
    __VAT_RATE = 0.19

    def _get_vat_rate(self):
        return self.__VAT_RATE   

    def get_size_rate_amount(self, order_item_size):
        match order_item_size:
            
            case OrderItemSize.SMALL:
                return  0.8
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.25
            #case OrderItemSize.XL:
                #return 1.4
            case OrderItemSize.XXL:
                return 1.3
            case _:
                raise Exception("This is not a valid order item size: " + order_item_size)
        
        return 1         


