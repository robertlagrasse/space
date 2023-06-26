import requests

class PhysicalLocation:
    def __init__(self, location):
        try:
            self.place_id = location["place_id"]
        except:
            self.place_id = None
        try:
            self.licence = location["licence"]
        except:
            self.licence = None
        try:
            self.osm_type = location["osm_type"]
        except:
            self.osm_type = None
        try:
            self.osm_id = location["osm_id"]
        except:
            self.osm_id = None
        try:
            self.lat = location["lat"]
        except:
            self.lat = None
        try:
            self.lon = location["lon"]
        except:
            self.lon = None
        try:
            self.display_name = location["display_name"]
        except:
            self.display_name = None
        try:
            self.address = location["address"]
        except:
            self.address = None
        try:
            self.house_number = location["address"]["house_number"]
        except:
            self.house_number = None
        try:
            self.road = location["address"]["road"]
        except:
            self.road = None
        try:
            self.town = location["address"]["town"]
        except:
            self.town = None
        try:
            self.state = location["address"]["state"]
        except:
            self.state = None
        try:
            self.postcode = location["address"]["postcode"]
        except:
            self.postcode = None
        try:
            self.country = location["address"]["country"]
        except:
            self.country = None
        try:
            self.country_code = location["address"]["country_code"]
        except:
            self.country_code = None
        try:
            self.ISO3166 = location["address"]["ISO3166-2-lvl4"]
        except:
            self.ISO3166 = None

class Geocoder:
    def __init__(self):
        self.api_url = "https://nominatim.openstreetmap.org/reverse?"

    def reverse(self, latitude, longitude, params=None):
        """Reverse geocode a latitude and longitude coordinate."""
        parameters = "&format=json"
        formatted_location = f"lat={str(latitude)}&lon={str(longitude)}"
        url = self.api_url + formatted_location + parameters
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

if __name__ == "__main__":
    geocoder = Geocoder()
    location = geocoder.reverse(40.712784, -74.005941)
    if location:
        print(location["address"])
