from django.shortcuts import render
from datetime import datetime
from .models import Announcement

from django.utils.translation import gettext as _, get_language


# Create your views here.


def home(request):
    print('Aktualni jazyk je:', get_language())
    current_i18n = str(get_language())
    announcements_query = Announcement.objects.values_list(current_i18n, 'created_at').order_by('created_at')[:4]
    announcements = [{"msg": x[0], "date": x[1].strftime('%d.%m.%Y')} for x in announcements_query]
    print(announcements)
    return render(
        request=request,
        template_name='base/home.html',
        context={"current_year": datetime.now().year,
                 "announcements": announcements}
    )
