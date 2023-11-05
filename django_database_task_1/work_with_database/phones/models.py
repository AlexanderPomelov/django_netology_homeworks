from pytils.translit import slugify
from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    image = models.ImageField(null=True)
    release_date = models.DateTimeField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name