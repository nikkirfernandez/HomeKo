# CODE HISTORY #
# Sontillano     # Feb 11, 2019     # added INFOTYPE_CHOICES, FEEDBACK_STATUS_CHOICES, REQUEST_STATUS_CHOICES

# File creation date: Feb. 11, 2019

INFOTYPE_CHOICES = (
     (1, (1)),     # AMENITY
     (2, (2)),     # FACILITY
     (3, (3)),     # RULE
)

FEEDBACK_STATUS_CHOICES = (
     (1, (1)),     # PENDING
     (2, (2)),     # APPROVED
     (3, (3)),     # NOT APPROVED
)

REQUEST_STATUS_CHOICES = (
     (1, (1)),     # NOT YET EVALUATED
     (2, (2)),     # CONTENT COMPLETE
     (3, (3)),     # CONTENT CORRECT
     (4, (4)),     # REQUEST DONE
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
