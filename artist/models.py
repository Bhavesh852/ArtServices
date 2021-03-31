from django.db import models

# Create your models here.

class Services(models.Model):
	s_id = models.AutoField(primary_key=True)
	service = models.CharField(max_length=100)
	s_image = models.ImageField(upload_to='artist/images')
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.service	


class Art(models.Model):
	a_id = models.AutoField(primary_key=True)
	a_name = models.CharField(max_length=30)
	a_price = models.IntegerField()
	a_service = models.ForeignKey(Services, on_delete=models.CASCADE)
	a_phone = models.IntegerField()
	a_address = models.CharField(max_length=120)
	a_condition = models.CharField(max_length=255)
	a_description = models.CharField(max_length=255)
	a_recentwork = models.ImageField(upload_to='artist/images')

	def __str__(self):
		return self.a_name


class Booking(models.Model):
	booking_id = models.AutoField(primary_key=True)
	booking_user = models.CharField(max_length=40)
	booking_phone = models.IntegerField()
	booking_address = models.CharField(max_length=255)
	booking_date_of_service = models.DateField()
	booking_service = models.ForeignKey(Art, on_delete=models.CASCADE)

class Contact(models.Model):
	c_id = models.AutoField(primary_key=True)
	c_name = models.CharField(max_length=40)
	c_email = models.EmailField(max_length=70)
	c_phone = models.IntegerField()
	c_msg = models.CharField(max_length=255)

	def __str__(self):
		return self.c_name