from django.shortcuts import render, redirect
from datetime import datetime
from .models import Announcement, GlobalSettings
from .forms import AnnouncementForm, AnnouncementsCountForm

from django.utils.translation import gettext as _, get_language
from django.contrib.auth import login, logout, authenticate


# { Handle Auth }
def handle_login(request):
    if request.user.is_authenticated:
        return redirect('main:webmanage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:webmanage')
            else:
                pass  # TODO messages

        return render(request, 'base/login.html')


def handle_logout(request):
    logout(request)
    return redirect('main:login')


# { Webmanage }
def webmanage(request):
    try:
        current_announcements_count = GlobalSettings.objects.get(key='announcements_count').value
        form = AnnouncementsCountForm(initial={'value': current_announcements_count})
    except GlobalSettings.DoesNotExist:
        form = AnnouncementsCountForm

    return render(
        request,
        'base/webmanage.html',
        {
            'announcements_count_form': form,
            'announcement_form': AnnouncementForm
        }
    )


# { Handle forms }

# def set_announcement_count_form(request):
#     """
#     Set how many announcement to display on Home page.
#     If there is not such setting stored in DB yet, the default value is 4.
#     """
#     if request.method == 'POST':
#         form_data = AnnouncementsCountForm(request.POST)
#
#         if form_data.is_valid():
#             value_from_form = {
#                 'value': form_data.data.get('value')
#             }
#
#             GlobalSettings.objects.update_or_create(value_from_form, key='announcements_count')
#             return redirect('main:webmanage')
#
#     return redirect('main:webmanage')  # TODO handle errors here - messages


def set_announcement_count_form(request):
    """
    Set how many announcement to display on Home page.
    If there is not such setting stored in DB yet, the default value is 4.
    """
    if request.method == 'POST':
        try:
            session = GlobalSettings.objects.get(key='announcements_count')
        except GlobalSettings.DoesNotExist:
            session = GlobalSettings(key='announcements_count')

        form_data = AnnouncementsCountForm(request.POST, instance=session)
        if form_data.is_valid():
            form_data.save()
            return redirect('main:webmanage')

    return redirect('main:webmanage')  # TODO handle errors here - messages


def add_announcement_form(request):
    """
    Create new announcement from the Webadmin page.
    """
    print(request)
    if request.method == 'POST':
        form_data = AnnouncementForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('main:webmanage')

    return redirect('main:home')  # TODO handle errors here - messages


# { Pages }
def home(request):

    # Read how many announcements to display from DB
    try:
        announcements_count = int(GlobalSettings.objects.get(key='announcements_count').value)
    except GlobalSettings.DoesNotExist:
        announcements_count = 1

    # Get current page language - i18n standard (cs, en, de)
    current_lang_i18n = str(get_language())

    # Query announcements as list of tuples (message, timestamp)
    announcements_query = Announcement.objects.values_list(current_lang_i18n, 'created_at').order_by('created_at')[0:announcements_count]
    announcements = [{"msg": x[0], "date": x[1].strftime('%d.%m.%Y')} for x in announcements_query]

    return render(
        request=request,
        template_name='base/home.html',
        context={"current_year": datetime.now().year,
                 "announcements": announcements}
    )


def accomodation(request):
    return render(
        request,
        'base/accomodation.html',
    )

# Endpoints
