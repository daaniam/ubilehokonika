from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import AnnouncementModel, GlobalSettingsModel
from .forms import AnnouncementForm, AnnouncementsCountForm

from django.utils.translation import gettext as _, get_language
from django.contrib.auth import login, logout, authenticate


# { Auth }
def auth_login(request):
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


def auth_logout(request):
    logout(request)
    return redirect('main:login')


# { Webmanage }
@login_required()
def webmanage(request):
    try:
        counts_from_db = GlobalSettingsModel.objects.get(key='announcements_count').value
        announcements_count_form = AnnouncementsCountForm(initial={'value': counts_from_db})
    except GlobalSettingsModel.DoesNotExist:
        announcements_count_form = AnnouncementsCountForm

    announcements = AnnouncementModel.objects.all()

    return render(
        request,
        'webmanage/webmanage.html',
        {
            'announcements_count_form': announcements_count_form,
            'announcement_form': AnnouncementForm,
            'announcements': announcements
        }
    )


# { Announcements }

# -- Second solution to Select form menu --

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

@login_required()
def announcement_set_count(request):
    """
    Set how many announcement to display on Home page.
    If there is not such setting stored in DB yet, the default value is 1.
    """
    if request.method == 'POST':
        try:
            session = GlobalSettingsModel.objects.get(key='announcements_count')
        except GlobalSettingsModel.DoesNotExist:
            session = GlobalSettingsModel(key='announcements_count')

        form_data = AnnouncementsCountForm(request.POST, instance=session)

        if form_data.is_valid():
            form_data.save()
            return redirect('main:webmanage')

    return redirect('main:webmanage')  # TODO handle errors here - messages


@login_required()
def announcement_create(request):
    form = AnnouncementForm()

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:webmanage')

    return render(
        request,
        'webmanage/announcement_form.html',
        {'form': form}
    )


@login_required()
def announcement_update(request, pk):
    announcement = AnnouncementModel.objects.get(id=pk)
    form = AnnouncementForm(instance=announcement)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('main:webmanage')

    return render(
        request,
        'webmanage/announcement_form.html',
        {
            'form': form
        }

    )


@login_required()
def announcement_delete(request, pk):
    if request.method == 'POST':
        announcement = AnnouncementModel.objects.get(id=pk)
        announcement.delete()

    return redirect('main:webmanage')


# { Pages }
def home(request):
    # Read how many announcements to display from DB.
    # If there is not such setting stored in DB yet, the default value is 1.
    try:
        announcements_count = int(GlobalSettingsModel.objects.get(key='announcements_count').value)
    except GlobalSettingsModel.DoesNotExist:
        announcements_count = 1

    # Get current page language - i18n standard (cs, en, de)
    current_lang_i18n = str(get_language())

    # Query announcements as list of tuples (message, timestamp)
    announcements_query = AnnouncementModel.objects.values_list(current_lang_i18n, 'created_at').order_by('created_at')[
                          0:announcements_count]

    announcements = [{"msg": x[0], "date": x[1].strftime('%d.%m.%Y')} for x in reversed(announcements_query)]

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
