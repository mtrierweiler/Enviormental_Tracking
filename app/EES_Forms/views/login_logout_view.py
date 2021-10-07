from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
import datetime
from ..models import user_profile_model, daily_battery_profile_model
from ..forms import CreateUserForm, user_profile_form
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

profile = user_profile_model.objects.all()


def register_view(request):
    if request.user.is_authenticated:
        return redirect('IncompleteForms')
    else:
        form = CreateUserForm()
        profile_form = user_profile_form()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            profile_form = user_profile_form(request.POST)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                profile.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('Login')
            else:
                messages.error(request, "The Information Entered Was Invalid.")
    return render(request, "ees_forms/ees_register.html", {
                'form': form, 'profile_form': profile_form
            })


def login_view(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    now = datetime.datetime.now()
    count_bp = daily_battery_profile_model.objects.count()

    if count_bp != 0:
        todays_log = daily_prof[0]

        if request.user.is_authenticated:
            if now.month == todays_log.date_save.month:
                if now.day == todays_log.date_save.day:
                    return redirect('IncompleteForms')
                else:
                    batt_prof = 'daily_battery_profile/login/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

                    return redirect(batt_prof)
            else:
                batt_prof = 'daily_battery_profile/login/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

                return redirect(batt_prof)

        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)

                    if now.month == todays_log.date_save.month:
                        if now.day == todays_log.date_save.day:
                            return redirect('IncompleteForms')
                        else:
                            batt_prof = 'daily_battery_profile/login/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

                            return redirect(batt_prof)
                    else:
                        batt_prof = 'daily_battery_profile/login/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

                        return redirect(batt_prof)
    else:
        batt_prof = 'daily_battery_profile/login/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

        return redirect(batt_prof)

    return render(request, "ees_forms/ees_login.html", {
         "now": now
    })


def logout_view(request):
    logout(request)

    return redirect('Login')


def profile_redirect(request):
    return redirect('profile/main')

    return render(request, 'profile.hmtl', {

    })


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'ees_forms/ees_password.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'access_page': 'success'})

    # success_url = reverse_lazy('profile')
