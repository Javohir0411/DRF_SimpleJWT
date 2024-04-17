from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class Food(models.Model):
    food_name = models.CharField(max_length=100, verbose_name='Taom nomi', null=False, blank=False)
    food_recipe = models.TextField(verbose_name='Taomning retsepti', null=True, blank=True, default='Kiritilmagan !')
    food_preparation = models.TextField(verbose_name='Taomning tayyorlanishi', null=True, blank=True)
    food_price = models.FloatField(verbose_name='Narxi', null=False, blank=False)
    food_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Taom turi", null=True)

    def __str__(self):
        return f"{self.pk} | {self.food_name}"

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
        db_table = 'food'
