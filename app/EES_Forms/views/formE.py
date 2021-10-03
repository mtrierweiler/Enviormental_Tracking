from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from ..models import Forms, user_profile_model, daily_battery_profile_model, formE_model
from ..forms import formE_form

lock = login_required(login_url='Login')
now = datetime.datetime.now()
back = Forms.objects.filter(form__exact='Incomplete Forms')


@lock
def formE(request, selector):
    profile = user_profile_model.objects.all()
    formName = "E"

    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')

    full_name = request.user.get_full_name()

    count_bp = daily_battery_profile_model.objects.count()

    if count_bp != 0:
        todays_log = daily_prof[0]
        if formE_model.objects.count() != 0:
            org = formE_model.objects.all().order_by('-date')
            database_form = org[0]
            if todays_log.date_save == database_form.date:
                initial_data = {
                    'observer': database_form.observer,
                    'date': database_form.date,
                    'crew': database_form.crew,
                    'foreman': database_form.foreman,
                    'start_time': database_form.start_time,
                    'end_time': database_form.end_time,
                    'leaks': database_form.leaks,
                    'oven1': database_form.oven1,
                    'time1': database_form.time1,
                    'source1': database_form.source1,
                    'comments1': database_form.comments1,
                }
                form = formE_form(initial=initial_data)

                if request.method == "POST":
                    check = formE_form(request.POST)
                    A_valid = check.is_valid()

                    if A_valid:
                        A = check.save()

                        if A.leaks == "Yes":
                            issue_page = '../../issues_view/E/' + str(database_form.date) + '/form'

                            return redirect(issue_page)

                        done = Forms.objects.filter(form='E')[0]
                        done.submitted = True
                        done.date_submitted = todays_log.date_save
                        done.save()

                        return redirect('IncompleteForms')

            else:
                initial_data = {
                    'date': todays_log.date_save,
                    'observer': full_name,
                    'crew': todays_log.crew,
                    'foreman': todays_log.foreman,
                }
                form = formE_form(initial=initial_data)
                done = Forms.objects.filter(form='E')[0]
                if request.method == "POST":
                    check = formE_form(request.POST)
                    A_valid = check.is_valid()

                    if A_valid:
                        A = check.save()

                        if A.leaks == "Yes":
                            issue_page = '../../issues_view/E/' + str(todays_log.date_save) + '/form'

                            return redirect(issue_page)

                        done = Forms.objects.filter(form='E')[0]
                        done.submitted = True
                        done.date_submitted = todays_log.date_save
                        done.save()

                        return redirect('IncompleteForms')
        else:
            initial_data = {
                'date': todays_log.date_save,
                'observer': full_name,
                'crew': todays_log.crew,
                'foreman': todays_log.foreman,
            }
            form = formE_form(initial=initial_data)
            done = Forms.objects.filter(form='E')[0]
            if request.method == "POST":
                check = formE_form(request.POST)
                A_valid = check.is_valid()

                if A_valid:
                    A = check.save()

                    if A.leaks == "Yes":
                        issue_page = '../../issues_view/E/' + str(todays_log.date_save) + '/form'

                        return redirect(issue_page)

                    done = Forms.objects.filter(form='E')[0]
                    done.submitted = True
                    done.date_submitted = todays_log.date_save
                    done.save()

                    return redirect('IncompleteForms')
    else:
        batt_prof = 'daily_battery_profile/login/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

        return redirect(batt_prof)

    return render(request, "Daily/formE.html", {
        "back": back, 'todays_log': todays_log, 'form': form, 'selector': selector, 'profile': profile, 'formName': formName
    })
