from django.db import models

class Additionalinfo(models.Model):
    additionalinfoid = models.AutoField(db_column='additionalInfoID', primary_key=True)  # Field name made lowercase.
    additionalinfoname = models.CharField(db_column='additionalInfoName', max_length=70)  # Field name made lowercase.
    additionalinfotype = models.IntegerFieldField(db_column='additionalInfoType', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'additionalInfo'

    def __str__(self):
        return "%s - $s" % (self.additionalinfoname, self.additionalinfotype)

class Area(models.Model):
    areaid = models.AutoField(db_column='areaID', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='areaName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area'

    def __str__(self):
        return self.areaname


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


class Contact(models.Model):
    contactid = models.AutoField(db_column='contactID', primary_key=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='contactNo', max_length=11)  # Field name made lowercase.
    ownerid = models.ForeignKey('Owner', models.DO_NOTHING, db_column='ownerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'

    def __str__(self):
        return "%s - %s" %(self.ownerid, self.contactno)


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


class Feedback(models.Model):
    feedbackid = models.AutoField(db_column='feedbackID', primary_key=True)  # Field name made lowercase.
    housingid = models.ForeignKey('Housing', models.DO_NOTHING, db_column='housingID')  # Field name made lowercase.
    comment = models.CharField(max_length=500)
    status = models.IntegerField()
    dateposted = models.DateField(db_column='datePosted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'



class Housetype(models.Model):
    housetypeid = models.AutoField(db_column='houseTypeID', primary_key=True)  # Field name made lowercase.
    housetypename = models.CharField(db_column='houseTypeName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'houseType'

    def __str__(self):
        return self.housetypename


class Housing(models.Model):
    housingid = models.AutoField(db_column='housingID', primary_key=True)  # Field name made lowercase.
    housingname = models.CharField(db_column='housingName', max_length=50)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='area')
    address = models.CharField(max_length=80)
    propertytype = models.ForeignKey('Propertytype', models.DO_NOTHING, db_column='propertyType')  # Field name made lowercase.
    housetype = models.ForeignKey(Housetype, models.DO_NOTHING, db_column='houseType')  # Field name made lowercase.
    maphtml = models.CharField(db_column='mapHTML', max_length=500, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='creationDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=45)  # Field name made lowercase.
    lasteditedby = models.CharField(db_column='lastEditedDate', max_length=45)  # Field name made lowercase.
    lastediteddate = models.DateField(db_column='lastEditedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'housing'

    def __str__(self):
        return self.housingname



class Propertytype(models.Model):
    propertytypeid = models.AutoField(db_column='propertyTypeID', primary_key=True)  # Field name made lowercase.
    propertytypename = models.CharField(db_column='propertyTypeName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertyType'

    def __str__(self):
        return self.propertytypename


class Request(models.Model):
    requestid = models.AutoField(db_column='requestID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField()
    message = models.CharField(max_length=500)
    status = models.IntegerField()
    datesent = models.DateField(db_column='dateSent')  # Field name made lowercase.
    sender = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'request'

    def __str__(self):
        return "%s - %s" % (self.sender, self.requestid)
