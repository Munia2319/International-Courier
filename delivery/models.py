from django.db import models


# Create your models here.
CHOICES = (
    ('DOX','DOX'),
    ('WPX', 'WPX'),)

countries = (
    ('USA','USA'),
    ('CANADA', 'CANADA'),
    ('AUSTRALIA', 'AUSTRALIA'),
    )

weights = (
    (0.5,'0.5'),
    (1.0, '1'),
    (1.5,'1.5'),
    (2.0, '2'),
    (2.5,'2.5'),
    (3.0, '3'),
    (3.5,'3.5'),
    (4.0, '4'),
    (4.5,'4.5'),
    (5.0, '5'),
    (5.5,'5.5'),
    (6.0, '6'),
    (6.5,'6.5'),
    (7.0, '7'),
    (7.5,'7.5'),
    (8.0, '8'),
    (8.5,'8.5'),
    (9.0, '9'),
    (9.5,'9.5'),
    (10.0, '10'),
    (10.5,'10.5'),
    (11.0, '11'),
    (11.5,'11.5'),
    (12.0, '12'),
    (12.5,'12.5'),
    (13.0, '13'),
    (13.5,'13.5'),
    (14.0, '14'),
    (14.5,'14.5'),
    (15.0, '15'),
    (15.5,'15.5'),
    (16.0, '16'),
    (16.5,'16.5'),
    (17.0, '17'),
    (17.5,'17.5'),
    (18.0, '18'),
    (18.5,'18.5'),
    (19.0, '19'),
    (19.5,'19.5'),
    (20.0, '20'),
    (20.5,'20.5'),
    (21.0, '21'),
    (21.5,'21.5'),
    (22.0, '22'),
    (22.5,'22.5'),
    (23.0, '23'),
    (23.5,'23.5'),
    (24.0, '24'),
    (24.5,'24.5'),
    (25.0, '25'),
    (25.5,'25.5'),
    (26.0, '26'),
    (26.5,'26.5'),
    (27.0, '27'),
    (27.5,'27.5'),
    (28.0, '28'),
    (28.5,'28.5'),
    (29.0, '29'),
    (29.5,'29.5'),
    (30.0, '30'),
    (31.0,'31'),
    )

class delivery_rate(models.Model):
	id = models.AutoField(primary_key=True)
	country= models.CharField(max_length=50, choices=countries, default='USA')
	delivery_type= models.CharField(max_length=50, choices=CHOICES, default='WPX')
	weight= models.DecimalField(max_digits=20, choices=weights, default='0.5',decimal_places=2)
	amount= models.DecimalField(max_digits=20, decimal_places=2)
	class Meta:
		db_table="delivery_delivery_rate"

class additional_charges(models.Model):
	id = models.BigIntegerField(primary_key=True)
	scheme_name= models.CharField(max_length=100)
	scheme_type= models.IntegerField(max_length=50)
	charge_per_transaction= models.FloatField()
	class Meta:
		db_table="delivery_additional_charges"

class products(models.Model):
    product_name=models.CharField(max_length=200)
    product_type=models.IntegerField()

    def __str__(self):
        return self.product_name



'''class order_info(models.Model):
    tracking_id=models.CharField(max_length=200)
    user_name=models.CharField(max_length=500)
    recipient_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    house_number=models.CharField(max_length=200)
    street_name=models.CharField(max_length=200)
    apartment_number=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    product_details=models.CharField(max_length=1000)
    delivery_type=models.CharField(max_length=200)
    pickup_date_start=models.CharField(max_length=200)
    pickup_date_end=models.CharField(max_length=200)
    delivery_status=models.CharField(max_length=200)
    payment_status=models.CharField(max_length=200)
    estimated_weight=models.FloatField()
    estimated_cost=models.FloatField()
    volumetric_weight=models.FloatField()
    payment_URL=models.CharField(max_length=1000)

    def __str__(self):
         return self.user_name'''

'''class  new_order_info(models.Model):

    tracking_id=models.CharField(max_length=200)
    user_name=models.CharField(max_length=500)
    sender_phn_number=models.CharField(max_length=500)
    recipient_name=models.CharField(max_length=200)
    recipient_email_1=models.CharField(max_length=200)
    recipient_email_2=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    house_number=models.CharField(max_length=200)
    street_name=models.CharField(max_length=200)
    apartment_number=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    product_details=models.CharField(max_length=1000)
    delivery_type=models.CharField(max_length=200)
    pickup_date_start=models.CharField(max_length=200)
    pickup_date_end=models.CharField(max_length=200)
    delivery_status=models.CharField(max_length=200)
    payment_status=models.CharField(max_length=200)
    estimated_weight=models.FloatField()
    estimated_cost=models.FloatField()
    volumetric_weight=models.FloatField()
    payment_URL=models.CharField(max_length=1000)
    company_phn_number=models.CharField(max_length=500)
    po_box=models.CharField(max_length=500)

    def __str__(self):
         return self.user_name'''

class  neww_order_info(models.Model):
    
    tracking_id=models.CharField(max_length=200)
    user_name=models.CharField(max_length=500)
    sender_phn_number=models.CharField(max_length=500)
    recipient_name=models.CharField(max_length=200)
    recipient_email_1=models.CharField(max_length=200)
    recipient_email_2=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    house_number=models.CharField(max_length=200)
    street_name=models.CharField(max_length=200)
    apartment_number=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    product_details=models.CharField(max_length=1000)
    delivery_type=models.CharField(max_length=200)
    pickup_date_start=models.CharField(max_length=200)
    pickup_date_end=models.CharField(max_length=200)
    delivery_status=models.CharField(max_length=200)
    payment_status=models.CharField(max_length=200)
    estimated_weight=models.FloatField()
    estimated_cost=models.FloatField()
    volumetric_weight=models.FloatField()
    payment_URL=models.CharField(max_length=1000)
    company_phn_number=models.CharField(max_length=500)
    po_box=models.CharField(max_length=500)
    payment_done=models.FloatField()

    def __str__(self):
         return self.user_name
    
class  order_info(models.Model):
    
    tracking_id=models.CharField(max_length=200)
    user_name=models.CharField(max_length=500)
    sender_name=models.CharField(max_length=100)
    sender_phn_number=models.CharField(max_length=500)
    sender_email=models.CharField(max_length=200)
    pick_country=models.CharField(max_length=200)
    pick_state=models.CharField(max_length=200)
    pick_town=models.CharField(max_length=200)
    pick_house_number=models.CharField(max_length=200)
    pick_street_name=models.CharField(max_length=200)
    pick_apartment_number=models.CharField(max_length=200)
    pick_zip_code=models.CharField(max_length=200)
    recipient_name=models.CharField(max_length=200)
    recipient_email_1=models.CharField(max_length=200)
    recipient_email_2=models.CharField(max_length=200)
    recipient_phone=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    house_number=models.CharField(max_length=200)
    street_name=models.CharField(max_length=200)
    apartment_number=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    product_details=models.CharField(max_length=1000)
    delivery_type=models.CharField(max_length=200)
    pickup_date_start=models.CharField(max_length=200)
    pickup_date_end=models.CharField(max_length=200)
    delivery_status=models.CharField(max_length=200)
    payment_status=models.CharField(max_length=200)
    estimated_weight=models.FloatField()
    estimated_cost=models.FloatField()
    volumetric_weight=models.FloatField()
    payment_URL=models.CharField(max_length=1000)
    po_box=models.CharField(max_length=500)
    payment_done=models.FloatField()

    def __str__(self):
         return self.user_name




class currency_rate(models.Model):
    currency_code=models.CharField(max_length=200)
    rate=models.FloatField()
   
    def __str__(self):
         return self.currency_code

class payment(models.Model):

    lowest_payment_rate=models.FloatField()
    
   








