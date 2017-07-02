from django.utils import timezone

from .forms import (ImageClickCountForm, UrlClickCountForm,
                    ButtonClickCountForm, UrlMonitoringForm)
from .models import (ImageClickCount, ButtonClickCount,
                     UrlClickCount, UrlMonitoring)


class CRUD(object):
    @staticmethod
    def update(data):
        return Update(data)

    @staticmethod
    def create(data):
        return Create(data)


class Update(object):
    def __init__(self, data):
        self.data = data

    def updateButton(self):
        name = self.data['name']
        description = self.data['description']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']

        try:
            instance = ButtonClickCount.objects.get(buttonName=name)
        except UrlMonitoring.DoesNotExist:
            return {
                'message':
                    'record didn\'t exist. Check your "state" key and values'
            }

        count = instance.count + 1

        form = ButtonClickCountForm({
            'buttonName': name,
            'buttonDescription': description,
            'count': count,
            'timeStamp': timezone.datetime.now(),
            'uID': uid,
            'userIP': ip,
            'userSession': session

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def updateURL(self):
        url = self.data['url']
        description = self.data['description']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']

        try:
            instance = UrlClickCount.objects.get(url=url)
        except UrlMonitoring.DoesNotExist:
            return {
                'message':
                    'record didn\'t exist. Check your "state" key and values'
            }

        count = instance.count + 1

        form = UrlClickCountForm({
            'url': url,
            'urlDescription': description,
            'count': count,
            'timeStamp': timezone.datetime.now(),
            'uID': uid,
            'userIP': ip,
            'userSession': session

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def updateImage(self):
        name = self.data['name']
        url = self.data['url']
        description = self.data['description']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']

        try:
            instance = ImageClickCount.objects.get(imageName=name,
                                                   imageURL=url)
        except UrlMonitoring.DoesNotExist:
            return {
                'message':
                    'record didn\'t exist. Check your "state" key and values'
            }

        count = instance.count + 1

        form = ImageClickCountForm({
            'imageURL': url,
            'imageDescription': description,
            'imageName': name,
            'count': count,
            'timeStamp': timezone.datetime.now(),
            'uID': uid,
            'userIP': ip,
            'userSession': session

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def updateUrlMonitoring(self):
        url = self.data['url']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']
        closeTime = self.data['close']

        try:
            instance = UrlMonitoring.objects.get(url=url, isClose=False)
        except UrlMonitoring.DoesNotExist:
            return {
                'message':
                    'record didn\'t exist. Check your \'state\' key and values'
            }

        form = UrlMonitoringForm({
            'url': url,
            'closeTime': closeTime,
            'openTime': instance.openTime,
            'timeStamp': timezone.datetime.now(),
            'uID': uid,
            'userIP': ip,
            'userSession': session,
            'isClose': True

        }, instance=instance)

        if form.is_valid():
            form.save()
            return {'message': 'user\'s visited time updated'}
        else:
            return {'message': form.errors}


class Create(object):
    def __init__(self, data):
        self.data = data

    def createImage(self):
        name = self.data['name']
        url = self.data['url']
        description = self.data['description']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']

        form = ImageClickCountForm({
            'imageURL': url,
            'imageDescription': description,
            'imageName': name,
            'count': 1,
            'uID': uid,
            'userIP': ip,
            'userSession': session
        })

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def createButton(self):
        name = self.data['name']
        description = self.data['description']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']

        form = ButtonClickCountForm({
            'buttonName': name,
            'buttonDescription': description,
            'count': 1,
            'uID': uid,
            'userIP': ip,
            'userSession': session
        })

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def createURL(self):
        url = self.data['url']
        description = self.data['description']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']

        form = UrlClickCountForm({
            'url': url,
            'urlDescription': description,
            'count': 1,
            'uID': uid,
            'userIP': ip,
            'userSession': session
        })

        if form.is_valid():
            form.save()
            return {'message': 'clicked save!'}
        else:
            return {'message': form.errors}

    def createUrlMonitoring(self):
        url = self.data['url']
        uid = self.data['uid']
        ip = self.data['ip']
        session = self.data['session']
        openTime = self.data['open']

        form = UrlMonitoringForm({
            'url': url,
            'closeTime': None,
            'openTime': openTime,
            'timeStamp': timezone.datetime.now(),
            'uID': uid,
            'userIP': ip,
            'userSession': session

        })

        if form.is_valid():
            form.save()
            return {'message': 'user\'s visited time saved'}
        else:
            return {'message': form.errors}
