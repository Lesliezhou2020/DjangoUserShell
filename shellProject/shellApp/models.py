from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''Eleanor Shellstrop = User.objects.create(
    first_name= 'Eleanor',
    last_name= 'Shellstrop',
    email_address= 'eleanor@shellstrop.com',
    age= 30,
)'''