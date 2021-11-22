
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    # Field name made lowercase.
    customer_id = models.IntegerField(
        db_column='Customer_id', primary_key=True)
    # Field name made lowercase.
    customer_gender = models.CharField(
        db_column='Customer_Gender', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    customer_income_group = models.CharField(
        db_column='Customer_Income_group', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    customer_region = models.CharField(
        db_column='Customer_Region', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    customer_marital_status = models.IntegerField(
        db_column='Customer_Marital_status', blank=True, null=True)

    class Meta:
        db_table = 'customers'


class PolicyDetails(models.Model):
    # Field name made lowercase.
    policy_id = models.IntegerField(db_column='Policy_ID', primary_key=True)
    # Field name made lowercase.
    date_of_purchase = models.DateField(
        db_column='Date_of_Purchase', blank=True, null=True)
    # Field name made lowercase.
    customer = models.ForeignKey(
        Customers, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)
    # Field name made lowercase.
    fuel = models.CharField(
        db_column='Fuel', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    vehicle_segment = models.CharField(
        db_column='VEHICLE_SEGMENT', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    premium = models.IntegerField(db_column='Premium', blank=True, null=True)
    bodily_injury_liability = models.IntegerField(blank=True, null=True)
    personal_injury_protection = models.IntegerField(blank=True, null=True)
    property_damage_liability = models.IntegerField(blank=True, null=True)
    collision = models.IntegerField(blank=True, null=True)
    comprehensive = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'policy_details'
