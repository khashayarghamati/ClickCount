from braces.views import CsrfExemptMixin, JSONRequestResponseMixin
from django.utils import timezone
from django.views import generic
from ipware.ip import get_ip

from .crud import CRUD
from .models import (ImageClickCount, ButtonClickCount, UrlClickCount)


class ClickView(generic.View, JSONRequestResponseMixin, CsrfExemptMixin):
    require_json = True

    def post(self, request, *args, **kwargs):
        try:

            self.type = request.POST.get('type', None)
            self.name = request.POST.get('name', None)
            self.description = request.POST.get('description', None)
            self.url = request.POST.get('url', None)
            self.uid = request.POST.get('uid', None)

            return self.render_json_response(self.chooseState())

        except KeyError:
            error_dict = {u"message": 'your keys aren\'t correct'}

            return self.render_bad_request_response(error_dict)

    def chooseState(self):
        data = {
            'name': self.name,
            'description': self.description,
            'url': self.url,
            'uid': self.uid,
            'ip': get_ip(request=self.request),
            'session': self.request.session.session_key
        }

        if self.type == 'image':
            if ImageClickCount.objects \
                    .filter(imageName=self.name, imageURL=self.url).exists():

                return CRUD.update(data=data).updateImage()
            else:
                return CRUD.create(data=data).createImage()

        elif self.type == 'button':
            if ButtonClickCount.objects.filter(buttonName=self.name).exists():
                return CRUD.update(data=data).updateButton()
            else:
                return CRUD.create(data=data).createButton()

        elif self.type == 'url':
            if UrlClickCount.objects.filter(url=self.url).exists():
                return CRUD.update(data=data).updateURL()
            else:
                return CRUD.create(data=data).createURL()


class UrlTimeDurationView(generic.View,
                          JSONRequestResponseMixin, CsrfExemptMixin):
    require_json = True

    def post(self, request, *args, **kwargs):
        try:

            self.session = self.request.session.session_key
            self.uID = request.POST.get('uid', None)
            self.url = request.POST.get('url', None)
            self.state = request.POST.get('state', None)

            return self.handleData()
        except KeyError:
            error_dict = {u"message": 'your keys aren\'t correct'}

            return self.render_bad_request_response(error_dict)

    def handleData(self):
        if self.state == 'open':
            data = {
                'session': self.session,
                'uid': self.uID,
                'url': self.url,
                'ip': get_ip(request=self.request),
                'close': None,
                'open': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            return self.render_json_response(
                CRUD.create(data=data).createUrlMonitoring()
            )
        else:
            data = {
                'session': self.session,
                'uid': self.uID,
                'url': self.url,
                'ip': get_ip(request=self.request),
                'close': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
                'open': 0
            }

            return self.render_json_response(
                CRUD.update(data).updateUrlMonitoring()
            )
