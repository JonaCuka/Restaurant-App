from base_enums import Location

class LocationManager:
    @staticmethod
    def get_location_from_string(location_as_string):
        for location in Location:
            if location.name == location_as_string:
                return location
        raise ("No location could be found for given location parameter")
        

    @staticmethod
    def get_location_from_id(location_id):
        for location in Location:
            if location.value == location_id:
                return location
        raise ("No location could be found for given location parameter Location ID :" + str(location_id))
        


