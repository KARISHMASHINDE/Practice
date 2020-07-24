from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    """ Represents food categories """

    category_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Food Category"
        
    def __str__(self):
        return self.category_name
        
        
class FoodDetails(models.Model):
    """ Represents food details """

    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="category_id")
    food_name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Food Details"
        
    def __str__(self):
            return self.food_name
