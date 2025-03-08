#Nmcasalett42 
#Parking:
#    Attributes: Name, location, type, total spots, permits issued, security features

#Transit Stop:
#    Attributes: Name, location, route number, schedule, transit type, accessibility options

#Landmark:
#    Attributes: Name, location, purpose, maintenance schedule, historical significance

#I bunched everything together here incase anything needs to be moved or deleted and can be moved to seperate files later#

class CampusFeature:
    """Base class representing a generic campus feature with a name and location."""
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} located at {self.location}"


class Parking(CampusFeature):
    """Represents a Parking feature on campus."""
    def __init__(self, name, location, parking_type, total_spots, permits_issued, security_features):
        super().__init__(name, location)
        self.parking_type = parking_type  # e.g., "multi-level", "open-air"
        self.total_spots = total_spots
        self.permits_issued = permits_issued
        self.security_features = security_features  # e.g., "CCTV, patrols"

    def __str__(self):
        return (f"Parking: {self.name} at {self.location} | Type: {self.parking_type}, "
                f"Total Spots: {self.total_spots}, Permits Issued: {self.permits_issued}, "
                f"Security: {self.security_features}")


class TransitStop(CampusFeature):
    """Represents a Transit Stop on campus."""
    def __init__(self, name, location, route_number, schedule, transit_type, accessibility_options):
        super().__init__(name, location)
        self.route_number = route_number
        self.schedule = schedule  # e.g., "Weekdays: 6am-10pm"
        self.transit_type = transit_type  # e.g., "bus", "shuttle"
        self.accessibility_options = accessibility_options  # e.g., "wheelchair accessible"

    def __str__(self):
        return (f"Transit Stop: {self.name} at {self.location} | Route Number: {self.route_number}, "
                f"Schedule: {self.schedule}, Transit Type: {self.transit_type}, "
                f"Accessibility: {self.accessibility_options}")


class Landmark(CampusFeature):
    """Represents a Landmark on campus."""
    def __init__(self, name, location, purpose, maintenance_schedule, historical_significance):
        super().__init__(name, location)
        self.purpose = purpose  # e.g., "monument", "historical marker"
        self.maintenance_schedule = maintenance_schedule  # e.g., "annual cleaning, monthly checks"
        self.historical_significance = historical_significance  # e.g., "built in 1920, site of key events"

    def __str__(self):
        return (f"Landmark: {self.name} at {self.location} | Purpose: {self.purpose}, "
                f"Maintenance: {self.maintenance_schedule}, Historical Significance: {self.historical_significance}")

# Usage and simple tests
if __name__ == "__main__":
    # Create instances of each class
    parking_instance = Parking(
        name="Central Parking Lot",
        location="North Campus",
        parking_type="Open-air",
        total_spots=150,
        permits_issued=120,
        security_features="CCTV, Patrols"
    )
    
    transit_stop_instance = TransitStop(
        name="Main Shuttle Stop",
        location="Campus Center",
        route_number="5A",
        schedule="Weekdays 7am-9pm",
        transit_type="Shuttle",
        accessibility_options="Wheelchair accessible"
    )
    
    landmark_instance = Landmark(
        name="Founders' Statue",
        location="Quad",
        purpose="Memorial",
        maintenance_schedule="Annual inspection",
        historical_significance="Dedicated to campus founders"
    )

    # Print the objects to test their __str__ representations
    print(parking_instance)
    print(transit_stop_instance)
    print(landmark_instance)