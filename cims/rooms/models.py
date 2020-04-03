from django.db import models
from datetime import datetime
# Create your models here.


class Rooms(models.Model):
    assets = (
    ('B', 'Bench'),
    ('T', 'Tube Light'),
    ('F', 'Fan'),
    ('C', 'Class Board'),
    ('S', 'Switch Board'),
    ('P', 'Projectors'),
    ('T', 'Table'),
    ('A', 'Almirah'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('MECH', 'MECH'),
    ('CIVIL', 'CIVIL'),
    ('IT', 'IT'),
    ('M', 'MISCELLANEOUS'),
)
    clg_code = models.CharField(max_length=200)
    block_no = models.CharField(max_length=200)
    room_no = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100, choices=assets)
    asset_no = models.CharField(max_length=20)
    unique_id = models.CharField(max_length=50, verbose_name='clg_code/block_no/room_no/asset_type/asset_no')
    description_asset = models.TextField(blank=True, verbose_name='Describe the asset if it is not clearly mentioned')
    price = models.IntegerField(blank=True)
    is_classroom = models.BooleanField(blank=True)
    is_lab = models.BooleanField(blank=True)
    is_staffroom = models.BooleanField(blank=True)
    is_other = models.BooleanField(blank=True)
    description_room = models.TextField(blank=True, verbose_name='Describe the Room if it is not clearly mentioned')
    date_of_purchase = models.DateTimeField(default=datetime.now, blank=True)
    manufacturing_date = models.DateTimeField(default=datetime.now, blank=True)
    warranty_date = models.DateTimeField(default=datetime.now, blank=True)
     
    def __str__(self):
        return self.unique_id
    

