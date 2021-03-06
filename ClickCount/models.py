from django.db import models

from .abstracts import (ButtonCountAbstract, ImageCountAbstract,
                        TimeStampAbstractModel, URLCountAbstract,
                        UserCommonInfoAbstracts)
from .utilities.strings import Strings


class ButtonClickCount(ButtonCountAbstract, TimeStampAbstractModel,
                       UserCommonInfoAbstracts):
    count = models.BigIntegerField(verbose_name=Strings.count_title)

    def __str__(self):
        return self.buttonName

    class Meta:
        verbose_name = Strings.buttonClickCount_title
        verbose_name_plural = Strings.buttonClickCount_plural_title


class ImageClickCount(ImageCountAbstract, TimeStampAbstractModel,
                      UserCommonInfoAbstracts):
    count = models.BigIntegerField(verbose_name=Strings.count_title)

    def __str__(self):
        return self.imageName

    class Meta:
        verbose_name = Strings.imageClickCount_title
        verbose_name_plural = Strings.imageClickCount_plural_title


class UrlClickCount(URLCountAbstract, TimeStampAbstractModel,
                    UserCommonInfoAbstracts):
    count = models.BigIntegerField(verbose_name=Strings.count_title)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = Strings.urlClickCount_title
        verbose_name_plural = Strings.urlClickCount_plural_title


class UrlMonitoring(TimeStampAbstractModel, UserCommonInfoAbstracts):
    url = models.URLField(unique=True, verbose_name=Strings.urlField_title)

    openTime = models.DateTimeField(
        verbose_name=Strings.openSpendTime_title)

    closeTime = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=Strings.closeSpendTime_title)

    isClose = models.BooleanField(default=False,
                                  verbose_name=Strings.isClose_title)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = Strings.urlMonitoring_plural_title
        verbose_name = Strings.urlMonitoring_Title
