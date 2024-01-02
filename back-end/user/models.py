# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class BoardConcern(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    contents = models.TextField()
    tag = models.CharField(max_length=75)
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_concern'


class BoardConsult(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    contents = models.TextField()
    tag = models.CharField(max_length=75)
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_consult'


class BoardReview(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    contents = models.TextField()
    tag = models.CharField(max_length=75)
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_review'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    board = models.ForeignKey(Board, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments'


class CommentsConcern(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    board = models.ForeignKey(BoardConcern, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments_concern'


class CommentsConsult(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    board = models.ForeignKey(BoardConsult, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments_consult'


class CommentsReview(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    board = models.ForeignKey(BoardReview, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments_review'

class Faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    contents = models.TextField()
    creationdate = models.DateTimeField()
    admin = models.ForeignKey(Admin, models.DO_NOTHING)

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
    gender = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'
