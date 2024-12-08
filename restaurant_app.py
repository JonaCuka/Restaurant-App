from base_model import Restaurant, Client, Menu
from order_utils import OrderPrinter, OrderManager
from menu_utils import MenuPrinter , MenuImporter
from location_utils import LocationManager
from calculator_utils import OrderCalculatorFactory
from custom_exeption import InvalidOrderItemSize
from base_enums import Location, ApplicationMode
from application_utils import ApplicationModeManager
   
class RestaurantApp:


    def __init__(self) -> None:
        self.__current_location =  None
        self.__file_path = "menu-list.csv"
#remove location_AS_STRING

    def start(self, application_mode ):   
        self.__current_location = self.get_current_location()
        application_mode = self.get_application_mode()
    
        try:
        #per ta ndare aplikacionin ne module perdorim CASE.
            match application_mode:
                case ApplicationMode.ORDER :
                    self.run_order_process()
                case ApplicationMode.TABLE_RESERVATION:
                    self.run_table_reservation_process()    
                case _: 
                    raise Exception("No valid alication modeis Selected!")   

        except InvalidOrderItemSize:
            print("The order Item size culdnt be determinded and the aplication cant't proced further")
    
    
    def get_current_location(self):
        print("Please select location (Type Number) : ")
        #location_options = "".join()
        for location in Location :
            print(str(location.value) + " " + location.name)
        location_id_input = input()
        

        try:
           location_id = int(location_id_input)
        except ValueError:
           raise Exception("Please provide the location by selecting the number")
        
        location = LocationManager.get_location_from_id(location_id)
        return location  # Return the actual location object
           
    def get_application_mode(self):
        print("Please select aplication mode: ")
        application_mode_options = "".join((str(application_mode.value )+ " " + application_mode.name + "\n" for application_mode in ApplicationMode ) )
        print(application_mode_options)
        application_mode_input_id = int(input())
        application_mode = ApplicationModeManager.get_application_mode_from_id(application_mode_input_id)
        return application_mode

    def run_order_process(self):
        restaurant = Restaurant("Sky Tower", "Rruga e Durrsit")
        client = Client("Jona", "0693284950")
        
        #menu = Menu()
        menu_importer = MenuImporter()
        menu = menu_importer.import_menu(self.__file_path)
        menuprinter = MenuPrinter()
        menuprinter.print_menu(menu)

        order_manager = OrderManager()
        order = order_manager.create_order(menu)
        order_manager.get_orders().append(order)

    
        self.__calculate_and_print_order_details( restaurant, client , order )
  

    def __calculate_and_print_order_details(self, restaurant, client , order   ):
        order_calculator = self.get_order_calculator()
        order_amount = order_calculator.calculate_order_amount(order)


        order_printer = OrderPrinter()   
        order_printer.print_order_info( restaurant, client, order, order_amount, order_calculator._get_vat_rate())



    def get_order_calculator(self):
        return  OrderCalculatorFactory.get_order_calculator_by_location(self.__current_location)
      

    def run_table_reservation_process(self):
        print("TABLE RESERVATION COMPLITED SUCCESSFULLY") 

restaurant_app = RestaurantApp()     
restaurant_app.start("ORDER")   