from django.db import models

#makes item list
TYPE_CHOICES = (        #tuple
    ('appetizers', 'appetizers'),
    ('entrees', 'entrees'),
    ('treats', 'treats'),
    ('drinks', 'drinks'),
)

class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default='', blank=True, null=False)
    description = models.TextField(max_length=500, default='', blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=0.00)
    image = models.CharField(max_length=255, default='', blank=True)
    #go to admin to register


    objects = models.Manager()

    def __str__(self):
        return self.name