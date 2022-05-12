from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    """ A category model for the product """

    class Meta:
        """ Display plural name correctly """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        """ A method to display name of the category """
        return self.name

    def get_friendly_name(self):
        """ A name to be displayed - explain better """
        return self.friendly_name


class Product(models.Model):
    """ A model for storing product attributes """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    color = ColorField(default='#FFE5B4')
    dimensions = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ A method to display name of the product """
        return self.name
