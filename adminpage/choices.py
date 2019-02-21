# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Feb 11, 2019     # added INFOTYPE_CHOICES, FEEDBACK_STATUS_CHOICES, REQUEST_TYPE_CHOICES, REQUEST_STATUS_CHOICES, TABLES_CHOICES

# File creation date: Feb. 11, 2019

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
     (1, ("Not yet evaluated")),     # NOT YET EVALUATED
     (2, ("Content complete")),     # CONTENT COMPLETE
     (3, ("Content correct")),     # CONTENT CORRECT
     (4, ("Request done")),     # REQUEST DONE
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
