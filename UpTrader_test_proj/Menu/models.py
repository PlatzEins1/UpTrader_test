from django.db import models

class menu_point(models.Model):
    url = models.CharField(max_length=50, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.url

# Create your models here.
