from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    first_name = models.CharField(_('first_name'), max_length=100, null=True, blank=True)
    second_name = models.CharField(_('second_name'), max_length=100, null=True, blank=True)
    third_name = models.CharField(_('third_name'), max_length=100, null=True, blank=True)
    birthday = models.DateField(_('birthday'), null=True, blank=True)

    def __str__(self):
        return '{first_name}, {third_name} ({birthday})'.format(
            first_name=self.first_name,
            third_name=self.third_name,
            birthday=self.birthday.strftime('%Y-%m-%d')
        )

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')


class Galery(models.Model):
    image = models.ImageField(_('photo'), upload_to='person_photo', null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='galery')

    class Meta:
        verbose_name = _('Galery')
        verbose_name_plural = _('Galeries')
