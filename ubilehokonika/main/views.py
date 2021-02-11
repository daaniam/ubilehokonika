from django.shortcuts import render
from datetime import datetime

from django.utils.translation import gettext as _


# Create your views here.


def home(request):
    return render(
        request=request,
        template_name='base/home.html',
        context={"current_year": datetime.now().year}
    )
