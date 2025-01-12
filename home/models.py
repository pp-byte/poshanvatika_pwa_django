from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.db.models.fields.files import ImageField
from django.core.exceptions import ValidationError
import easygui
import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

# def validate_image(image):
#     file_size = image.file.size
#     limit_mb = 15
#     if file_size > limit_mb * 1024 * 1024:
#         easygui.msgbox("Upload image lesser than 15 MB", title="Warning!")
#         raise ValidationError("Max size of file is %s MB" % limit_mb)

class UploadPictureModel(models.Model):
    picture = models.ImageField(upload_to='PoshanVatikaPics/', blank=True, null=True, default='PoshanVatikaPics/noImage.jpg')
    name = models.CharField(max_length=100, default='')
    nutri_nm = models.CharField(max_length=100, default='')
    area = models.IntegerField()
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(UploadPictureModel, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture
    def __str__(self):
        return self.nutri_nm

class UploadWellPictureModel(models.Model):
    picture = models.ImageField( upload_to='WellPics/', blank=True, null=True, default='WellPics/noImage.jpg')
    name = models.CharField(max_length=100, blank=True, null=True)
    well_nm = models.CharField(max_length=100, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(UploadWellPictureModel, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture


class PoshanFormInformation(models.Model):
    organization_name = models.CharField(max_length=100)
    district_village_taluka_name = models.CharField(max_length=100)
    pin_code = models.IntegerField(blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    type_of_nutri = models.CharField(max_length=50)
    name_of_ngo = models.CharField(max_length=100)
    area_nutri_garden = models.CharField(max_length=100)
    seasonal_veg_name = models.CharField(max_length=100)
    perennial_veg_name = models.CharField(max_length=100)
    fruits_name = models.CharField(max_length=100)
    month_earnings = models.IntegerField(blank=True, null=True)
    level_nutri_garden = models.CharField(max_length=100)
    nutri_garden_scale=models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'poshan_form_information'
    def __str__(self):
        return self.organization_name