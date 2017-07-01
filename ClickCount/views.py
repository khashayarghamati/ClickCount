from braces.views import CsrfExemptMixin, JSONRequestResponseMixin
from django.views import generic

from .crud import CRUD
from .models import ImageClickCount, ButtonClickCount, UrlClickCount


class ClickView(generic.View, JSONRequestResponseMixin, CsrfExemptMixin):
    require_json = True

    def post(self, request, *args, **kwargs):
        try:

            self.type = request.POST.get('type', None)
            self.name = request.POST.get('name', None)
            self.description = request.POST.get('description', None)
            self.url = request.POST.get('url', None)

            return self.render_json_response(self.chooseState())

        except KeyError:
            error_dict = {u"message": 'your keys aren\'t correct'}

            return self.render_bad_request_response(error_dict)

    def chooseState(self):
        crud = CRUD(self.url, self.name, self.description)

        if self.type == 'image':
            if ImageClickCount.objects \
                    .filter(imageName=self.name, imageURL=self.url).exists():

                return crud.update().updateImage()
            else:
                return crud.create().createImage()

        elif self.type == 'button':
            if ButtonClickCount.objects.filter(buttonName=self.name).exists():
                return crud.update().updateButton()
            else:
                return crud.create().createButton()

        elif self.type == 'url':
            if UrlClickCount.objects.filter(url=self.url).exists():
                return crud.update().updateURL()
            else:
                return crud.create().createURL()


class UrlCountShowView(generic.View,
                       JSONRequestResponseMixin, CsrfExemptMixin):
    require_json = True

    def post(self):
        pass  # todo in developing
