from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from menu_utils import MenuImporter
from kivy.core.window import Window
from kivy.lang import Builder


class RestaurantAppGUI(MDApp):

    __selected_product = None

    def build(self):
        
        Window.size = (500, 700)
        #screen = Screen()
        screen = Builder.load_file("restaurant_app_gui.kv")

        menu_importer = MenuImporter()
        menu = menu_importer.import_menu('menu-list.csv')

        #gets all the product data.
        product_list = list(menu.get_menu_items().values())
        #then create a list which we will add all the taken data
        table_row_data = []
        #Loops over each product in the list and then append function to add the datas 
        #For each product, appends a tuple to the table_row_data list, where each tuple contains the product's ID, name, and price.
        for product in product_list:
            table_row_data.append((product.get_product_id(), product.get_name(), product.get_price()))
        
        # menu_table is an instance of MDDataTable, which is a table widget for displaying data in rows and columns.
        menu_table = MDDataTable(
            #Set the data table position
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            #set the datatable size 
            size_hint = (0.9 , 0.8),
            #Enables checkboxes in each row. This means the table will have checkboxes next to each row.
            check = True,
            #Defines the columns of the table. Each tuple in this list represents a column:
            column_data = [
                #three columns : id, name, price
                ("Id", dp(30)),
                ("Name", dp(75)),
                ("Price", dp(30))

            ],
            #Passes the table_row_data list to populate the rows of the table. This list contains the product ID, name, and price for each row.
            row_data = table_row_data,
            #Specifies the number of rows to be displayed in the table. If you have fewer rows than this, it will still show 10 rows but with empty rows after the data ends.
            rows_num = 10
        )    
        menu_table.bind(on_check_press=self.checked)
        menu_table.bind(on_row_press=self.on_row_press)

        #screen.add_widget(menu_table)
        #Add menu data table to kivy file screen
        screen.children[0].add_widget(menu_table)
        return screen 
    
    def checked(self, instant_table, current_row):
        print(current_row)


    def on_row_press(self, instance_table, instance_row):
        row_number = int(instance_row.index/len(instance_table.column_data))
        self.__selected_product = instance_table.row_data[row_number]
    
        self.get_text_fields_layout().children[2].text = str(self.__selected_product)
        self.get_text_fields_layout().children[1].text = str(self.__selected_product)
        self.get_text_fields_layout().children[0].text = str(self.__selected_product)
    
    def get_text_fields_layout(self):
        md_card = self.root.children[0] 
        general_box_layout = md_card.children[1]
        text_field_layout = general_box_layout.children[1]
        return text_field_layout
    
RestaurantAppGUI().run() 

      