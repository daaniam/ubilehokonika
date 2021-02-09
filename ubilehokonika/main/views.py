from django.shortcuts import render
from django.utils.translation import gettext as _


# Create your views here.


def home(request):
    output = _("Hello there")
    return render(
        request=request,
        template_name='base/home.html',
        context=None
    )
