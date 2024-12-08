from base_model import Meal, Drink, Menu
import csv
from custom_exeption import InvalidMenuFile


class MenuPrinter:
    def print_menu(self, menu):
        menu_items = menu.get_menu_items()
        for key in menu_items:
            product = menu_items[key]  
            if isinstance(product, Meal):
                decription_text = "" if product.get_decription() == "" else "( " + product.get_decription() + ")"
                print(str(product.get_product_id()) + "." + product.get_name() + decription_text + " | " + str(product.get_price()) + " euro")
            elif isinstance(product, Drink):
                sugar_free_text = "yes" if product.is_sugar_free() else "no"
                print(str(product.get_product_id()) + "." + product.get_name() + "(Sugar free: " + sugar_free_text + ")" + " | " + str(product.get_price()) + " Euro")


class MenuImporter:
    def import_menu(self, file_path):
        #open the csv file based in file path *(location)
        menu_file = open(file_path)
        csv_reader = csv.reader(menu_file)
        return self._transform_csv_menu_data_to_menu(csv_reader)
    
     #References (callers of)
    def _transform_csv_menu_data_to_menu(self, csv_reader):
        imported_menu = Menu(True)
        for row in csv_reader:
            product_id = int(row[0])
            product_name = row[1]
            product_price = float(row[2])
            product_category = row[3]

   
            # implement product category if\ else
            if "meal" == product_category:
                product = Meal(product_id, product_name, product_price, "")
            elif "drink" == product_category:
                sugar_free = row[4]
                product = Drink(product_id, product_name, product_price, sugar_free)
            else:

                # Standard Libraries feature: join(string)
                exception_message = "".join("The menu file couldn't be processed as the the product category from product "
                                            .join (product_name)
                                            .join("is invalid."))
                raise InvalidMenuFile(exception_message)

            imported_menu.get_menu_items().update({product_id: product})

        return imported_menu 