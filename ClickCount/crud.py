from django.shortcuts import get_object_or_404
from django.utils import timezone

from .forms import ImageClickCountForm, UrlClickCountForm, ButtonClickCountForm
from .models import ImageClickCount, ButtonClickCount, UrlClickCount


class CRUD(object):
    def __init__(self, url, name, description):
        self.url = url
        self.name = name
        self.description = description

    def update(self):
        return Update(self.url, self.name, self.description)

    def create(self):
        return Create(self.url, self.name, self.description)


class Update(object):
    def __init__(self, url, name, description):
        self.url = url
        self.name = name
        self.description = description

    def updateButton(self):
        instance = get_object_or_404(ButtonClickCount, buttonName=self.name)
        count = instance.count + 1

        form = ButtonClickCountForm({
            'buttonName': self.name,
            'buttonDescription': self.description,
            'count': count,
            'timeStamp': timezone.now()

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def updateURL(self):
        instance = get_object_or_404(UrlClickCount, url=self.url)
        count = instance.count + 1

        form = UrlClickCountForm({
            'url': self.url,
            'urlDescription': self.description,
            'count': count,
            'timeStamp': timezone.now()

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def updateImage(self):
        instance = get_object_or_404(ImageClickCount, imageName=self.name,
                                     imageURL=self.url)
        count = instance.count + 1

        form = ImageClickCountForm({
            'imageURL': self.url,
            'imageDescription': self.description,
            'imageName': self.name,
            'count': count,
            'timeStamp': timezone.now()

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}


class Create(object):
    def __init__(self, url, name, description):
        self.url = url
        self.name = name
        self.description = description

    def createImage(self):
        form = ImageClickCountForm({
            'imageURL': self.url,
            'imageDescription': self.description,
            'imageName': self.name,
            'count': 1,
        })

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def createButton(self):
        form = ButtonClickCountForm({
            'buttonName': self.name,
            'buttonDescription': self.description,
            'count': 1,
        })

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def createURL(self):
        form = UrlClickCountForm({
            'url': self.url,
            'urlDescription': self.description,
            'count': 1,
        })

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}
