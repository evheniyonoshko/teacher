from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Person, Galery


class GaleryInline(admin.TabularInline):
    model = Galery
    extra = 1
    verbose_name = _('Photo')
    verbose_name_plural = _('Photos')
    classes = ('collapse',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'third_name', 'birthday')
    inlines = [GaleryInline, ]


admin.site.register(Person, PersonAdmin)
