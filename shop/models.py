from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class CategoryManager(models.Manager):
    """
    manager class for Category model
    """

    def active(self):
        """
        active method for Category manager
        """
        return self.filter(status=True)


class MenuItemManager(models.Manager):
    """
    manager class for MenuItem model
    """

    def active(self):
        """
        active method for MenuItem manager
        """
        return self.filter(status=True)


class Category(models.Model):
    """
    Category model
    """
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="زیردسته")
    title = models.CharField(max_length=64, verbose_name="عنوان")
    description = models.TextField(
        null=True, blank=True, verbose_name="توضیحات")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # thumbnail = models.ImageField(upload_to='category', verbose_name="تصویر")

    objects = CategoryManager()

    class Meta:
        """
        Meta class for Category
        """
        ordering = ['-status']
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def items_count(self):
        """
        returns count of MenuItems related to Category
        """
        return self.items.count()
    items_count.short_description = "تعداد"

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    """
    MenuItem model
    """
    title = models.CharField(max_length=64, verbose_name="عنوان")
    thumbnail = models.ImageField(upload_to='menu', verbose_name="تصویر")
    categories = models.ForeignKey(
        Category, related_name='items', verbose_name="دسته بن دیها", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(
        validators=[MinValueValidator(1000)], verbose_name="قیمت")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = MenuItemManager()

    class Meta:
        """
        Meta class
        """
        ordering = ['-status']
        verbose_name = "آیتم غذا"
        verbose_name_plural = "آیتم های غذا"

    @property
    def persian_digit_price(self):
        """
        replace digits of price with Persian digits
        """
        digits = {
            "0": "۰",
            "1": "۱",
            "2": "۲",
            "3": "۳",
            "4": "۴",
            "5": "۵",
            "6": "۶",
            "7": "۷",
            "8": "۸",
            "9": "۹",
        }
        result = ""
        for i, digit in enumerate(reversed(str(self.price)), start=1):
            result += digits[digit]
            if i % 3 == 0 and i != len(str(self.price)):
                result += "،"
        return ''.join(reversed(result))

    def __str__(self):
        return self.title
