from django.db import models
from django.conf import settings

class Href(models.Model):
    href_name = models.CharField(verbose_name='Имя ссылки', max_length=200)
    href_adress = models.CharField(verbose_name='Адрес ссылки', max_length=1000)

    def __str__(self):
        return self.href_name
 
    class Meta:
        verbose_name_plural = 'Ссылки'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mail_notifications = models.BooleanField(verbose_name='Уведомления по E-mail')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)