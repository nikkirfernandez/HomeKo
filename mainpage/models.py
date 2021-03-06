# License: MIT License
# CODE HISTORY #
# Kasilag     # Feb 3, 2019     #Patterened from Database SQL Dump

# File creation date: Feb. 3, 2019


from django.db import models
from .choices import *

# This class contains the table for additionalInfo
class Additionalinfo(models.Model):
    additionalinfoid = models.AutoField(db_column='additionalInfoID', primary_key=True)
    additionalinfoname = models.CharField(db_column='additionalInfoName', max_length=70)
    additionalinfotype = models.IntegerField(db_column='additionalInfoType', choices = INFOTYPE_CHOICES)

    class Meta:
        managed = False
        db_table = 'additionalinfo'
    # For Readability
    def __str__(self):
        return self.additionalinfoname

    def is_deletable(self):
        for rel in self._meta.get_fields():
            try:
                related = rel.related_model.objects.filter(**{rel.field.name: self})
                if related.exists():
                    return False
            except AttributeError: 
                pass 
        return True

# This class contains the table for Areas designated to each housing entry in the database
class Area(models.Model):
	areaid = models.AutoField(db_column='areaid', primary_key=True)
	areaname = models.CharField(db_column='areaname', max_length=30)

	class Meta:
		managed = False
		db_table = 'area'

	def __str__(self):
		return self.areaname

	def is_deletable(self):
		for rel in self._meta.get_fields():
			try:
				related = rel.related_model.objects.filter(**{rel.field.name: self})
				if related.exists():
					return False
			except AttributeError: 
				pass 
		return True

# The Following Classes are generated for MySQL

class AuthGroup(models.Model):
	name = models.CharField(unique=True, max_length=80)

	class Meta:
		managed = False
		db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
	permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_group_permissions'
		unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
	name = models.CharField(max_length=255)
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
	codename = models.CharField(max_length=100)

	class Meta:
		managed = False
		db_table = 'auth_permission'
		unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_user_groups'
		unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_user_user_permissions'
		unique_together = (('user', 'permission'),)

#####################################################################################


# This class contains the attributes for the Owner Table to be added to the connected MySQL Database
class Owner(models.Model):
	ownerid = models.AutoField(db_column='ownerID', primary_key=True)  # Field name made lowercase.
	ownername = models.CharField(db_column='ownerName', max_length=70)  # Field name made lowercase.
	firstname = models.CharField(db_column='firstName', max_length=40)  # Field name made lowercase.
	lastname = models.CharField(db_column='lastName', max_length=40)  # Field name made lowercase.
	email = models.CharField(max_length=60, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'owner'

	def __str__(self):
		return self.ownername

	def is_deletable(self):
		for rel in self._meta.get_fields():
			try:
				related = rel.related_model.objects.filter(**{rel.field.name: self})
				if related.exists():
					return False
			except AttributeError: 
				pass 
		return True


#This class contains the attributes for Owner Table to be added to the connected MySQL Database
class Contact(models.Model):
	contactid = models.AutoField(db_column='contactID', primary_key=True)  # Field name made lowercase.
	contactno = models.CharField(db_column='contactNo', max_length=11)  # Field name made lowercase.
	ownerid = models.ForeignKey('Owner', on_delete=models.CASCADE, db_column='ownerID')  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'contact'

	def __str__(self):
		return "%s - %s" % (self.ownerid, self.contactno)


# The Following classes are automatically generated by django

class DjangoAdminLog(models.Model):
	action_time = models.DateTimeField()
	object_id = models.TextField(blank=True, null=True)
	object_repr = models.CharField(max_length=200)
	action_flag = models.PositiveSmallIntegerField()
	change_message = models.TextField()
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'django_admin_log'


class DjangoContentType(models.Model):
	app_label = models.CharField(max_length=100)
	model = models.CharField(max_length=100)

	class Meta:
		managed = False
		db_table = 'django_content_type'
		unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
	app = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	applied = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_migrations'


class DjangoSession(models.Model):
	session_key = models.CharField(primary_key=True, max_length=40)
	session_data = models.TextField()
	expire_date = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_session'


#############################################################################################

#This class contains the attributes for Feedback Table to be added to the connected MySQL Database
class Feedback(models.Model):
	feedbackid = models.AutoField(db_column='feedbackID', primary_key=True)  # Field name made lowercase.
	housingid = models.ForeignKey('Housing', on_delete=models.CASCADE, db_column='housingID')  # Field name made lowercase.
	comment = models.CharField(max_length=500, db_column='comment')
	status = models.IntegerField(db_column='status', choices = FEEDBACK_STATUS_CHOICES)
	dateposted = models.DateField(db_column='datePosted')  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'feedback'


#This class contains the attributes for HouseType Table to be added to the connected MySQL Database
class Housetype(models.Model):
	housetypeid = models.AutoField(db_column='houseTypeID', primary_key=True)  # Field name made lowercase.
	housetypename = models.CharField(db_column='houseTypeName', max_length=20)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'housetype'

	def __str__(self):
		return self.housetypename

	def is_deletable(self):
		for rel in self._meta.get_fields():
			try:
				related = rel.related_model.objects.filter(**{rel.field.name: self})
				if related.exists():
					return False
			except AttributeError: 
				pass 
		return True

#This class contains the attributes for Housing Table to be added to the connected MySQL Database
class Housing(models.Model):
	housingid = models.AutoField(db_column='housingID', primary_key=True)  # Field name made lowercase.
	housingname = models.CharField(db_column='housingName', max_length=50)  # Field name made lowercase.
	area = models.ForeignKey(Area, on_delete=models.CASCADE, db_column='area')
	address = models.CharField(db_column='address', max_length=80)
	propertytype = models.ForeignKey('Propertytype', on_delete=models.CASCADE, db_column='propertyType')  # Field name made lowercase.
	housetype = models.ForeignKey(Housetype, on_delete=models.CASCADE, db_column='houseType')  # Field name made lowercase.
	maphtml = models.CharField(db_column='mapHTML', max_length=500, blank=True, null=True)  # Field name made lowercase.
	
	class Meta:
		managed = False
		db_table = 'housing'

	def __str__(self):
		return self.housingname

	def is_deletable(self):
		for rel in self._meta.get_fields():
			try:
				related = rel.related_model.objects.filter(**{rel.field.name: self})
				if related.exists():
					return False
			except AttributeError: 
				pass 
		return True

#This class contains the attributes for Propertytype Table to be added to the connected MySQL Database
class Propertytype(models.Model):
	propertytypeid = models.AutoField(db_column='propertyTypeID', primary_key=True)  # Field name made lowercase.
	propertytypename = models.CharField(db_column='propertyTypeName', max_length=20)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'propertytype'

	def __str__(self):
		return self.propertytypename

	def is_deletable(self):
		for rel in self._meta.get_fields():
			try:
				related = rel.related_model.objects.filter(**{rel.field.name: self})
				if related.exists():
					return False
			except AttributeError: 
				pass 
		return True

#This class contains the attributes for Request Table to be added to the connected MySQL Database
class Request(models.Model):
	requestid = models.AutoField(db_column='requestID', primary_key=True)  # Field name made lowercase.
	reqtype = models.IntegerField(db_column='type', choices = REQUEST_TYPE_CHOICES)
	message = models.CharField(db_column='message', max_length=500)
	status = models.IntegerField(db_column='status', choices = REQUEST_STATUS_CHOICES)
	datesent = models.DateField(db_column='dateSent')  # Field name made lowercase.
	sender = models.CharField(db_column='sender', max_length=50)

	class Meta:
		managed = False
		db_table = 'request'

	def __str__(self):
		return "%s - %s" % (self.reqtype, self.message[0:20])

	def is_deletable(self):
		for rel in self._meta.get_fields():
			try:
				related = rel.related_model.objects.filter(**{rel.field.name: self})
				if related.exists():
					return False
			except AttributeError: 
				pass 
		return True

#This class contains the attributes for HousingAdditionalInfo Table to be added to the connected MySQL Database
class HousingAdditionalInfo(models.Model):
	housingadditionalinfoid = models.AutoField(db_column='housingAdditionalInfoID', primary_key=True)
	additionalinfoid = models.ForeignKey(Additionalinfo, on_delete=models.CASCADE, db_column='additionalInfoID')
	description = models.CharField(max_length=300, db_column='description', blank=True, null=True)
	housingid = models.ForeignKey(Housing, on_delete=models.CASCADE, db_column='housingID')

	class Meta:
		managed = False
		db_table = 'housingadditionalinfo'

#This class contains the attributes for HousingOwner Table to be added to the connected MySQL Database
class HousingOwner(models.Model):
	housingownerid = models.AutoField(db_column='HousingOwnerID', primary_key=True)
	housingid = models.ForeignKey(Housing, on_delete=models.CASCADE, db_column='housingID')
	ownerid = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='ownerID')

	class Meta:
		managed = False
		db_table = 'housingowner'

#This class contains the attributes for HousingRequest Table to be added to the connected MySQL Database
class HousingRequest(models.Model):
	housingrequestid = models.AutoField(db_column='HousingRequestID', primary_key=True)
	housingid = models.ForeignKey(Housing, on_delete=models.CASCADE, db_column='housingID')
	requestid = models.ForeignKey(Request, on_delete=models.CASCADE, db_column='requestID')

	class Meta:
		managed = False
		db_table = 'housingrequest'

#This class contains the attributes for Picture Table to be added to the connected MySQL Database
class Picture(models.Model):
	pictureid = models.AutoField(db_column='pictureID', primary_key=True)
	filename = models.CharField(db_column='fileName', max_length=30)
	housingid = models.ForeignKey(Housing, on_delete=models.CASCADE, db_column='housingID')

	class Meta:
		managed = False
		db_table = 'picture'

#This class contains the attributes for RoomCost Table to be added to the connected MySQL Database
class RoomCost(models.Model):
	roomid = models.AutoField(db_column='roomID', primary_key=True)
	roomname = models.CharField(db_column='roomName', max_length=100)
	cost = models.FloatField(db_column='cost')
	housingid = models.ForeignKey(Housing, on_delete=models.CASCADE, db_column='housingID')

	class Meta:
		managed = False
		db_table = 'roomcost'
