# License: MIT License
# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added AREA_CHOICES, PROPERTY_CHOICES, HOME_CHOICES, AMENITY_CHOICES, FACILITY_CHOICES, RULE_CHOICES

# File creation date: Feb. 5, 2019

AREA_CHOICES = (
     (1, ("Anywhere")),
     (2, ("Area 1")),
     (3, ("Area 2")),
     (4, ("Hardin ng Doña Aurora")),
     (5, ("Kapitbalay ng Kalinaw")),
     (6, ("Pook Dagohoy")),
     (7, ("Pook Palaris")),
     (8, ("Pook Ricarte")),
     (9, ("Village A")),
     (10, ("Village B")),
)

PROPERTY_CHOICES = (
     (1, ("Anything")),
     (2, ("House")),
     (3, ("Apartment")),
)

HOME_CHOICES = (
     (1, ("Anything")),
     (2, ("Entire place")),
     (3, ("Private room")),
     (4, ("Shared room")),
)

AMENITY_CHOICES = (
     (1, ("Kitchen")),
     (2, ("Air conditioning")),
     (3, ("Washer")),
     (4, ("Dryer")),
     (5, ("Wifi")),
     (6, ("Iron")),
     (7, ("TV")),
)

FACILITY_CHOICES = (
     (1, ("Parking")),
)

RULE_CHOICES = (
     (1, ("Pets allowed")),
     (2, ("Smoking allowed")),
     (3, ("No curfew")),
)

INFOTYPE_CHOICES = (
     (1, ("Amenity")),     # AMENITY
     (2, ("Facility")),     # FACILITY
     (3, ("Rule")),     # RULE
)

FEEDBACK_STATUS_CHOICES = (
     (1, ("Pending")),     # PENDING
     (2, ("Approved")),     # APPROVED
     (3, ("Not Approved")),     # NOT APPROVED
)

REQUEST_TYPE_CHOICES = (
     (1, ("Add")),     # ADD
     (2, ("Update")),     # UPDATE
     (3, ("Delete")),     # DELETE
)

REQUEST_STATUS_CHOICES = (
     (1, ("Pending")),     # NOT YET EVALUATED
     (2, ("In progress")),     # collecting info from owner
     (3, ("Done")),     # request executed
     (4, ("Not Approved")),     # NOT APPROVED
)

TABLES_CHOICES = (
     (1, ("Additionalinfo")),     
     (2, ("Area")),     
     (3, ("Contact")),     
     (4, ("Feedback")),
     (5, ("Housetype")),     
     (6, ("HousingAdditionalinfo")),     
     (7, ("HousingOwner")),     
     (8, ("HousingRequest")),
     (9, ("Housing")),     
     (10, ("Owner")),     
     (11, ("Picture")),     
     (12, ("Propertytype")),
     (13, ("Request")),     
     (14, ("RoomCost")),     
)

