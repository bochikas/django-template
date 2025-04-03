import logging

from django.db import models
from django.utils.functional import classproperty

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    @classproperty
    def app_label(cls):  # noqa
        return cls._meta.app_label  # noqa

    @classproperty
    def model_name(cls):  # noqa
        return cls._meta.model_name  # noqa

    @classmethod
    def get_field(cls, field_name):
        return cls._meta.get_field(field_name)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class IsActiveModel(BaseModel):
    is_active = models.BooleanField(default=True, verbose_name="Активно?")

    active_objects = ActiveManager()
    objects = models.Manager()

    class Meta:
        abstract = True


class CreatedAtModel(BaseModel):
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True, blank=True)

    class Meta:
        abstract = True


class UpdatedAtModel(BaseModel):
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True, blank=True)

    class Meta:
        abstract = True


class TimeStampedModel(CreatedAtModel, UpdatedAtModel):
    class Meta:
        abstract = True


class IsActiveTimeStampedModel(TimeStampedModel, IsActiveModel):
    class Meta:
        abstract = True
