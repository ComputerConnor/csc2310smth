#MonotonicIodine

class Business:
    def __init__(self, name, location, __revenue, operating_hours, floor_spaces):
        self.name = name
        self.location = location
        self.__revenue = __revenue
        self.operating_hours = operating_hours
        self.floor_spaces = floor_spaces
        # possible methods here

class Bookstore(Business):
    def __init__(self,name, location, __revenue, operating_hours, floor_spaces, __inventory_size, employee_count, university_merchandise):
        super().__init__(name, location, __revenue, operating_hours, floor_spaces)
        self.__inventory_size = __inventory_size
        self.employee_count = employee_count
        self.university_merchandise = university_merchandise
        # possible methods here

class Retail(Business):
    def __init__(self, name, location, __revenue, operating_hours, floor_spaces, product_category, customer_capacity, payment_methods):
        super().__init__(name, location, __revenue, operating_hours, floor_spaces)
        self.product_category = product_category
        self.customer_capacity = customer_capacity
        self.payment_methods = payment_methods
        # possible methods here

class Food(Business):
    def __init__(self, name, location, __revenue, operating_hours, floor_spaces,  cuisine_type, seating_capacity, accepted_meal_plans):
        super().__init__(name, location, __revenue, operating_hours, floor_spaces)
        self.cuisine_type = cuisine_type
        self.seating_capacity = seating_capacity
        self.accepted_meal_plans = accepted_meal_plans
        # possible methods here