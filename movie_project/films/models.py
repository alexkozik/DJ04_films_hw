from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    review = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return self.title