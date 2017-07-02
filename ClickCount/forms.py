from django.forms import ModelForm

from .models import (ImageClickCount, ButtonClickCount,
                     UrlClickCount, UrlMonitoring)


class ImageClickCountForm(ModelForm):
    class Meta:
        model = ImageClickCount
        fields = ['imageURL', 'imageDescription', 'imageName',
                  'count', 'timeStamp', 'uID', 'userIP', 'userSession']


class ButtonClickCountForm(ModelForm):
    class Meta:
        model = ButtonClickCount
        fields = ['buttonName', 'buttonDescription', 'count',
                  'timeStamp', 'uID', 'userIP', 'userSession']


class UrlClickCountForm(ModelForm):
    class Meta:
        model = UrlClickCount
        fields = ['url', 'urlDescription', 'count', 'timeStamp',
                  'uID', 'userIP', 'userSession']


class UrlMonitoringForm(ModelForm):
    class Meta:
        model = UrlMonitoring
        fields = ['url', 'openTime', 'closeTime', 'timeStamp', 'uID',
                  'userIP', 'userSession', 'isClose']
