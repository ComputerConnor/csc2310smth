#MonotonicIodine
#Business
#    Attributes: Name, location, revenue, operating hours, floor spaces
#    Bookstore:
#        Attributes: Inventory size, number of employees, affiliated university merchandise
#    Retail:
#        Attributes: Product categories, customer capacity, payment methods
#    Food:
#        Attributes: Cuisine type, seating capacity, meal plans accepted
Class Business:
def __init__(self, name, location, __revenue, operating_hours, floor_spaces)
    self.name = name
    self.location = location
    self.__revenue = __revenue
    self.operating_hours = operating_hours
    self.floor_spaces = floor_spaces
# possible methods here

Class Bookstore(Business):
def __init__(self, __inventory_size, employee_count, university_merchandise)
    super.init().__init__()
    self.__inventory_size = __inventory_size
    self.employee_count = employee_count
    self.university_merchandise = university_merchandise 
