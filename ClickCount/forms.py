from django.forms import ModelForm

from .models import ImageClickCount, ButtonClickCount, UrlClickCount


class ImageClickCountForm(ModelForm):
    class Meta:
        model = ImageClickCount
        fields = ['imageURL', 'imageDescription', 'imageName',
                  'count', 'timeStamp']


class ButtonClickCountForm(ModelForm):
    class Meta:
        model = ButtonClickCount
        fields = ['buttonName', 'buttonDescription', 'count', 'timeStamp']


class UrlClickCountForm(ModelForm):
    class Meta:
        model = UrlClickCount
        fields = ['url', 'urlDescription', 'count', 'timeStamp']
