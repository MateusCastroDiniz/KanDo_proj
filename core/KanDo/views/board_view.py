from django.http import HttpResponse
from django.views import generic


class BoardView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<div style="font-family: Sans-Serif, Verdana; width:100%; '
                            'height: 100%; display:flex; align-items:center; flex-direction: column;'
                            'justify-content: center"><h1 style="color:green">Hello World!</h1>'
                            '<p style="color:green; font-size:20px">Página tá vivaaaa!!!</p></div>')
