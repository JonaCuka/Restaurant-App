from base_model import Order, OrderItems
from base_enums import OrderItemSize

class OrderPrinter:
    def __print_order_item_info(self, order_item):
        product = order_item.get_product()  # Use the instance method on the order_item
        print(str(order_item.get_quantity()) + " x " + product.get_name() + " | " + str(product.get_price()) + " Euro")

    def __print_order_item_header(self, client):  
        print("----------------------------------------------------")  
        print("Order from " + str(client.get_name()) + " . ")
        print("Contact Number " + str(client.get_phone_nr()))
        print(".......................................................")

    def __print_order_info_footer(self, restaurant, order_amount, vat_rate):   
        print(".......................................................")
        print("the total price of the order is: ")
        print("SUB Total: " + str(order_amount.get_total_order_amount()))
        print("VAT " + str(vat_rate) + "% " + str(order_amount.get_total_order_amount_vat()))
        print("Total: " + str(order_amount.get_total_order_amount_with_vat()))
        print(".......................................................")    
        print("From " + restaurant.get_name() + " in " + restaurant.get_address())

    def print_order_info(self, restaurant, client, order, order_amount, vat_rate):
        self.__print_order_item_header(client)
        order_products = order.get_order_items()  
        for order_product in order_products:
            self.__print_order_item_info(order_product)
        self.__print_order_info_footer(restaurant, order_amount, vat_rate)

    
# duhet te krijojme kete klasen per metoden get dhe set  
class OrderAmount:
    def __init__(self, total_order_amount, total_order_amount_vat, total_order_amount_with_vat ):
        #deklarojme variablia si atribute
        self.__total_order_amount = total_order_amount
        self.__total_order_amount_vat = total_order_amount_vat
        self.__total_order_amount_with_vat = total_order_amount_with_vat

    def get_total_order_amount(self): 
        return self.__total_order_amount 
    
    def get_total_order_amount_vat(self): 
        return self.__total_order_amount_vat 

    def get_total_order_amount_with_vat(self): 
        return self.__total_order_amount_with_vat
    

class OrderManager:
    def __init__(self):
        self.__orders = []

#akesesimi i array me get 
    def get_orders(self):
        return self.__orders  


#krijojme metoden per te per te krijuar nje porosi, produket  marrim nga objekti order
    def create_order(self, menu):
        order = Order()
         
        self.add_order_item(order, menu.get_menu_items().get(100), 1, OrderItemSize.XXL)
        self.add_order_item(order, menu.get_menu_items().get(101), 1 , OrderItemSize.MEDIUM)
        self.add_order_item(order, menu.get_menu_items().get(200), 2 , OrderItemSize.LARGE)
        self.add_order_item(order, menu.get_menu_items().get(201), 3 , OrderItemSize.SMALL)
       # 

        return order

    def add_order_item(self, order, product, quantity, order_item_size):
        order_item = self.create_order_item(product, order_item_size, quantity)
        order.get_order_items().append(order_item)

    def create_order_item(self, product, order_item_size, quantity):
        order_item = OrderItems(product, order_item_size, quantity)
        return order_item


    def add_order(self, order):

        index = 0
        while index <= len(self.__order_list):
            if self.__order_list[index]  == None:
               self.__order_list[index] = order
               return
            index += 1
                  
