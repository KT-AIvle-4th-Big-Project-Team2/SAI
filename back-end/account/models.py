# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=75)
    password = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'admin'


class Announcements(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=45)
    admin = models.ForeignKey(Admin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'announcements'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    contents = models.TextField()
    tag = models.CharField(max_length=75)
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    board = models.ForeignKey(Board, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments'


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
    id = models.BigAutoField(primary_key=True)
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


class Faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    content = models.TextField()
    creationdate = models.DateTimeField()
    admin_admin = models.ForeignKey(Admin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faq'


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    contents_ai = models.TextField()
    user_user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report'


class Suggestions(models.Model):
    suggetion_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    content = models.TextField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        db_table = 'suggestions'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=75)
    password = models.CharField(max_length=75)
    email = models.CharField(max_length=254)
    phonenumber = models.CharField(max_length=11)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length = 1)

    class Meta:
        managed = False
        db_table = 'user'
