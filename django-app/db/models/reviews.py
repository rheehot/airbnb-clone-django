from django.conf import settings
from django.db import models
from core import models as core_models
from db.models import Room

__all__ = (
    'Review',
)


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField(
        blank=True,
    )
    accuracy = models.IntegerField(
        default=0,
    )
    communication = models.IntegerField(
        default=0,
    )
    cleanliness = models.IntegerField(
        default=0,
    )
    location = models.IntegerField(
        default=0,
    )
    check_in = models.IntegerField(
        default=0,
    )
    value = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
    )
