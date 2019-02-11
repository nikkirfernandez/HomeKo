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
     (3, (3)),     # REQUEST DONE
)
