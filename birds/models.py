from django.db import models


class BirdModel(models.Model):
    name = models.CharField('Название', max_length=60, unique=True)
    image = models.ImageField('Фото', upload_to='media/', blank=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()  # переводим полученное в верхний регист
        return super(BirdModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class AddBirdModel(models.Model):
    bird = models.ForeignKey(BirdModel, on_delete=models.CASCADE, verbose_name='Птица')
    quantity = models.PositiveIntegerField('Количество', default=1)
    city = models.CharField('Город', max_length=60, default=None)
    region = models.CharField('Район', max_length=60, default=None)
    street = models.CharField('Улица', max_length=60, default=None)
    created = models.DateTimeField('Создано', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.city = self.city.title()
        self.region = self.region.title()
        self.street = self.street.title()
        return super(AddBirdModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.bird)
