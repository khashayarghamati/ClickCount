from django.utils import timezone
from django.db import models

from .utilities.strings import Strings
from .validators import (buttonNameValidator, urlValidator,
                         imageNameValidator, imageUrlValidator)


class TimeStampAbstractModel(models.Model):
    timeStamp = models.DateTimeField(default=timezone.datetime.now,
                                     verbose_name=Strings.timeStamp_title)

    class Meta:
        abstract = True


class ButtonCountAbstract(models.Model):

    buttonName = models.CharField(max_length=50,
                                  unique=True,
                                  validators=[buttonNameValidator],
                                  verbose_name=Strings.buttonName_title)

    buttonDescription = models.CharField(max_length=1000,
                                         blank=True,
                                         verbose_name=Strings.
                                         buttonDescription_title)

    class Meta:
        abstract = True


class URLCountAbstract(models.Model):

    url = models.URLField(unique=True,
                          validators=[urlValidator],
                          verbose_name=Strings.urlField_title)

    urlDescription = models.CharField(max_length=1000,
                                      null=True,
                                      blank=True,
                                      verbose_name=Strings.
                                      urlDescription_title)

    class Meta:
        abstract = True


class ImageCountAbstract(models.Model):

    imageName = models.CharField(max_length=50,
                                 unique=True,
                                 validators=[imageNameValidator],
                                 verbose_name=Strings.imageName_title)

    imageURL = models.URLField(unique=True,
                               validators=[imageUrlValidator],
                               verbose_name=Strings.imageUrlField_title)

    imageDescription = models.CharField(max_length=1000,
                                        blank=True,
                                        verbose_name=Strings.
                                        imageDescription_title)

    class Meta:
        abstract = True


class UserCommonInfoAbstracts(models.Model):

    uID = models.IntegerField(blank=True,
                              null=True,
                              verbose_name=Strings.uID_title)

    userIP = models.GenericIPAddressField(default='1270.0.1',
                                          verbose_name=Strings.userIP_title)

    userSession = models.CharField(max_length=500,
                                   blank=True,
                                   verbose_name=Strings.userSession_title)

    class Meta:
        abstract = True
