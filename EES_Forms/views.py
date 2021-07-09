from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from operator import itemgetter
import datetime
from .models import *
from .forms import *


daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
todays_log = daily_prof[0]
lock = login_required(login_url='Login')
back = Forms.objects.filter(form__exact='Incomplete Forms')

#------------------------------------------------------------------------REGISTER---------<
# Create your views here.
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
#--------------------------------------------------------------------------------LOGIN---------<
def login_view(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    if request.user.is_authenticated:
        if now.month == todays_log.date_save.month:
            if now.day == todays_log.date_save.day:
                return redirect('IncompleteForms')  
            else:
                return redirect('daily_battery_profile')
        else:
                return redirect('daily_battery_profile')
        
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                
                login(request, user)
                #return redirect('daily_battery_profile')
                
                if now.month == todays_log.date_save.month:
                    if now.day == todays_log.date_save.day:
                        return redirect('IncompleteForms')  
                    else:
                        return redirect('daily_battery_profile')
                else:
                        return redirect('daily_battery_profile')
    return render(request, "ees_forms/ees_login.html", {
         "now": now
    })
#-------------------------------------------------------------------------BATTERY PROFILE---------<
@lock
def daily_battery_profile_view(request):
    
    form = daily_battery_profile_form
    if request.method =='POST':
        form = daily_battery_profile_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('IncompleteForms')
    
    return render (request, "ees_forms/Bat_info.html",{
        'form': form
    })
#----------------------------------------------------------------------------------LOGOUT---------<
def logout_view(request):
    logout(request)
    return redirect ('Login')
#------------------------------------------------------------------------INCOMPLETE FORMS---------<
@lock
def IncompleteForms(request):
    now = datetime.datetime.now()
    sub_forms = Forms.objects.all()
    print(now.date())
    print(sub_forms[0].date_submitted)
    
    
    for forms in sub_forms:
        A = forms.date_submitted
        if now.date() != A :
            forms.submitted = False
            forms.save()
            

    pull = Forms.objects.filter(submitted__exact=False).order_by('form')
    pullNot = Forms.objects.filter(submitted__exact=True).order_by('form')
    
    
    
    
    
    
    return render(request, "ees_forms/index.html", {
        "pull": pull, "pullNot":pullNot, "now": now, 'todays_log': todays_log, "back": back, 'sub_forms':sub_forms
    })

#------------------------------------------------------------------ADMIN PUSH TRAVELS-------------<
def pt_admin1_view(request):
    reads = subA5_readings_model.objects.all()
    data = subA5_model.objects.all()
    #add_days = datetime.timedelta(days=91)
    
    
    def all_ovens(reads):
        A = []
        for items in reads:
            date = items.form.date
            date_array = date.split("-")
            
            year = int(date_array[0])
            month = int(date_array[1])
            day = int(date_array[2])
            
            form_date = datetime.datetime(year, month, day)
            added_date = form_date + datetime.timedelta(days=91)
            due_date = added_date - datetime.datetime.now() 
            
            if len(str(items.o1)) == 1 :
                oven1 = "0" + str(items.o1)
            else:
                oven1 = items.o1
            A.append((oven1, items.form.date, added_date.date, due_date.days)) 
            
            if len(str(items.o2)) == 1 :
                oven2 = "0" + str(items.o2)
            else:
                oven2 = items.o2
            A.append((oven2, items.form.date, added_date.date, due_date.days))
                
            if len(str(items.o3)) == 1 :
                oven3 = "0" + str(items.o3)
            else:
                oven3 = items.o3
            A.append((oven3, items.form.date, added_date.date, due_date.days))    
                
            if len(str(items.o4)) == 1 :
                oven4 = "0" + str(items.o4)
            else:
                oven4 = items.o4
            A.append((oven4, items.form.date, added_date.date, due_date.days))      

        return A      
    hello = all_ovens(reads)
    func = lambda x: (x[0], x[1])
    sort = sorted(hello, key = func, reverse=True)
    
    def final(sort):
        B = []
        i = 1
        for new in sort:
            B.append(new)
        for x in sort:
            for y in range(i, len(sort)):
                tree = sort[y]
                if tree[0] == x[0]:
                    B.remove(tree)
            i+=1
        return B
    cool = final(sort)
        
        
    
   
    return render(request, "ees_forms/PushTravels.html", {
        "now": now, 'todays_log': todays_log, "back": back, 'reads': reads, 'data': data, 'cool': cool
    })
#------------------------------------------------------------------------ADMIN DATA-------------<
@lock
def admin_data_view(request):
    return render (request, "ees_forms/admin_data.html", {
        "back": back, 'todays_log': todays_log 
    })
#------------------------------------------------------------------------A1---------------<
@lock
def formA1(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    full_name = request.user.get_full_name()
    initial_data = {
        'date' : todays_log.date_save,
        'observer' : full_name,
        'crew' : todays_log.crew,
        'foreman' : todays_log.foreman,
    }
    data = subA1_form(initial=initial_data)
    readings = subA1_readings_form()
    #ptadmin = pt_admin1_form()
    if request.method == "POST":
        form = subA1_form(request.POST)
        reads = subA1_readings_form(request.POST)
        #admin = pt_admin1_form(request)
        A_valid = form.is_valid()
        B_valid = form.is_valid()
        #c_valid = admin.is_valid()
        if A_valid and B_valid:# and C_valid:
            A = form.save()
            B = reads.save(commit=False)
            B.form = A
            B.save()
            
            done = Forms.objects.filter(form='A-1')[0]
            done.submitted = True
            done.save()
           # D = admin.save(commit=False)
           # D.form = C
            #D.save()
            return redirect('IncompleteForms')
    else:
        form = subA1_form(initial=initial_data)
        readings = subA1_readings_form()
        ptadmin = pt_admin1_form()
    return render (request, "Daily/Method303/formA1.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'readings': readings
    })
#------------------------------------------------------------------------A2---------------<
@lock
def formA2(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    return render (request, "Daily/Method303/formA2.html", {
        "back": back, 'todays_log': todays_log
    })
#------------------------------------------------------------------------A3---------------<
@lock
def formA3(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    return render (request, "Daily/Method303/formA3.html", {
        "back": back, 'todays_log': todays_log
    })
#------------------------------------------------------------------------A4---------------<
@lock
def formA4(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    return render (request, "Daily/Method303/formA4.html", {
        "back": back, 'todays_log': todays_log
    })
#------------------------------------------------------------------------A5---------------<
@lock
def formA5(request):
    this_from = 'A-5'
    
    full_name = request.user.get_full_name()
    cert_date = request.user.user_profile_model.cert_date
    initial_data = {
        'date' : todays_log.date_save,
        'estab' : "EES COKE BATTERY",
        'county' : "Wayne",
        'estab_no' : "P0408",
        'equip_loc' : "Zug Island",
        'district' : "Detroit",
        'city' : "River Rouge",
        'observer' : full_name,
        'cert_date' : cert_date,
        'process_equip1' : "Coke Battery / Door Machine / Hot Car",
        'process_equip2' : "Door Machine / PECS",
        'op_mode1' : "normal",
        'op_mode2' : "normal",
        'emission_point_start' : "Above hot car",
        'emission_point_stop' : "Above door machine hood",
        'height_above_ground' : "45",
        'height_rel_observer' : "45",
        'plume_type' : 'N/A', 
        'water_drolet_present' : "No",
        'water_droplet_plume' : "N/A",
        'plume_opacity_determined_start' : "Above hot car",
        'plume_opacity_determined_stop' : "Above door machine hood",
        'describe_background_start' : "Skies",
        'describe_background_stop' : "Same"
    }
    data = subA5_form(initial=initial_data)
    profile_form = user_profile_form()
    readings_form = subA5_readings_form()
    
    if request.method == "POST":
        form = subA5_form(request.POST)
        readings = subA5_readings_form(request.POST)
        A_valid = form.is_valid()
        B_valid = readings.is_valid()
        if A_valid and B_valid:
            A = form.save()
            B = readings.save(commit=False)

            B.form = A
            B.save()
            done = Forms.objects.filter(form='A-5')[0]
            done.submitted = True
            done.save()
            
            return redirect('IncompleteForms')
    else:
        form = subA5_form(initial=initial_data)
        readings_form = subA5_readings_form()
    return render (request, "Daily/Method303/formA5.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'profile_form': profile_form, 'readings_form': readings_form
    })
#------------------------------------------------------------------------FORM B---------------<
@lock
def formB(request):
    return render (request, "Daily/formB.html", {
        "back": back
    })
#------------------------------------------------------------------------FORM C---------------<
@lock
def formC(request):
    submitted = False
    if request.method == "POST":
        CReadings = FormCReadForm(request.POST)
        CData = SubFormC1(request.POST)
        A_valid = CReadings.is_valid()
        B_valid = CData.is_valid()
        #form.save()
        #return HttpResponseRedirect('./formC?submitted=True')
        if A_valid and B_valid:
            A = CData.save()
            B = CReadings.save(commit=False)
            B.form = A
            B.save()
            return HttpResponseRedirect('./formC?submitted=True')
    else:
        form = SubFormC1
        read = FormCReadForm
        if 'submitted' in request.GET:
            submitted = True
    return render (request, "Daily/formC.html", {
        'form': form, 'read': read, 'submitted': submitted, "back": back, 'now': now
    })

#------------------------------------------------------------------------FORM D---------------<
@lock
def formD(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    today = datetime.date.today()
    last_friday = today - datetime.timedelta(days=today.weekday() + 2)
    one_week = datetime.timedelta(days=6)
    end_week = last_friday + one_week
    
    week_start_dates = formD_model.objects.all().order_by('-week_start')
    week_almost = week_start_dates[0]
    week = week_almost.week_start
    
    if week == last_friday:
        data = week_almost
        empty_form = formD_form()
        if request.method == "POST":
            form = formD_form(request.POST)
            A_valid = form.is_valid()
            if A_valid:
                A = request.POST
                for key, value in A.items():
                    print({key : value})
                print(week_almost.__dict__.keys())
                    
                #for key2, value2 in week_almost:
                    #print(key2, value2)
                    #if week_almost.key == value:
                        
                    #print(key)
                    #print(value)
                
                
                #week_almost.truck_id3 = A.truck_id3
                
                #week_almost.save()
                
                
                
                
                #B = week_almost.save()
                #A.truck_id3 = week_almost.truck_id3
                
                #A.save()
                
                
                
                return redirect('IncompleteForms')

    else:
        initial_data = {
            'week_start' : last_friday,
            'week_end' : end_week
        }
        data = formD_form()
        empty_form = formD_form(initial= initial_data)
        if request.method == "POST":
            form = formD_form(request.POST)
            A_valid = form.is_valid()
            if A_valid:
                form.save()

                return redirect('IncompleteForms')
        
    return render (request, "Daily/formD.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'empty': empty_form, 'week': week, 'last_friday': last_friday, 'week_almost': week_almost, 'end_week': end_week
    })
#----------------------------------------------------------------------FORM E---------------<
@lock
def formE(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    full_name = request.user.get_full_name()
    initial_data = {
        'date' : todays_log.date_save,
        'observer' : full_name,
        'crew' : todays_log.crew,
        'foreman' : todays_log.foreman,
    }
    model = formE_form(initial=initial_data)
    done = Forms.objects.filter(form='E')[0]
    if request.method == "POST":
        check = formE_form(request.POST)
        #admin = pt_admin1_form(request)
        A_valid = check.is_valid()
        print(done)
        if A_valid:
            check.save()
            done.submitted = True
            done.save()
            

            return redirect('IncompleteForms')
    else:
        model = formE_form(initial=initial_data)
    return render (request, "Daily/formE.html", {
        "back": back, 'todays_log': todays_log, 'model': model,
    })

#----------------------------------------------------------------------FORM G1---------------<
@lock
def formG1(request):    
    full_name = request.user.get_full_name()
    cert_date = request.user.user_profile_model.cert_date
    initial_data = {
        'date' : todays_log.date_save,
        'estab' : "EES COKE BATTERY",
        'county' : "Wayne",
        'estab_no' : "P0408",
        'equip_loc' : "Zug Island",
        'district' : "Detroit",
        'city' : "River Rouge",
        'observer' : full_name,
        'cert_date' : cert_date,
        'process_equip1' : "-",
        'process_equip2' : "-",
        'op_mode1' : "normal",
        'op_mode2' : "normal",
        'emission_point_start' : "Above Stack",
        'emission_point_stop' : "Same",
        'height_above_ground' : "150",
        'height_rel_observer' : "150",
        'water_drolet_present' : "No",
        'water_droplet_plume' : "N/A",
        'describe_background_start' : "Skies",
        'describe_background_stop' : "Same"
    }
    data = formG1_form(initial=initial_data)
    profile_form = user_profile_form()
    readings_form = subA5_readings_form()
    
    if request.method == "POST":
        form = formG1_form(request.POST)
        #readings = subA5_readings_form(request.POST)
        A_valid = form.is_valid()
        #B_valid = readings.is_valid()
        if A_valid:# and B_valid:
            A = form.save()
            #B = readings.save(commit=False)

            #B.form = A
            #B.save()
            done = Forms.objects.filter(form='G-1')[0]
            done.submitted = True
            done.save()
            
            return redirect('IncompleteForms')
    else:
        form = formG1_form(initial=initial_data)
        #readings_form = subA5_readings_form()
    return render (request, "Daily/formG1.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'profile_form': profile_form, #'readings_form': readings_form
    })


#----------------------------------------------------------------------FORM H---------------<
@lock
def formH(request):    
    full_name = request.user.get_full_name()
    cert_date = request.user.user_profile_model.cert_date
    initial_data = {
        'date' : todays_log.date_save,
        'estab' : "EES COKE BATTERY",
        'county' : "Wayne",
        'estab_no' : "P0408",
        'equip_loc' : "Zug Island",
        'district' : "Detroit",
        'city' : "River Rouge",
        'observer' : full_name,
        'cert_date' : cert_date,
        'process_equip1' : "-",
        'process_equip2' : "-",
        'op_mode1' : "normal",
        'op_mode2' : "normal",
        'emission_point_start' : "Above Stack",
        'emission_point_stop' : "Same",
        'height_above_ground' : "300",
        'height_rel_observer' : "300",
        'water_drolet_present' : "No",
        'water_droplet_plume' : "N/A",
        'describe_background_start' : "Skies",
        'describe_background_stop' : "Same"
    }
    data = formH_form(initial=initial_data)
    profile_form = user_profile_form()
    readings_form = subA5_readings_form()
    
    if request.method == "POST":
        form = formH_form(request.POST)
        #readings = subA5_readings_form(request.POST)
        A_valid = form.is_valid()
        #B_valid = readings.is_valid()
        if A_valid:# and B_valid:
            A = form.save()
            #B = readings.save(commit=False)

            #B.form = A
            #B.save()
            done = Forms.objects.filter(form='H')[0]
            done.submitted = True
            done.save()
            
            return redirect('IncompleteForms')
    else:
        form = formH_form(initial=initial_data)
        #readings_form = subA5_readings_form()
    return render (request, "Daily/formH.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'profile_form': profile_form, #'readings_form': readings_form
    })

#----------------------------------------------------------------------FORM I---------------<
@lock
def formI(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    today = datetime.date.today()
    last_friday = today - datetime.timedelta(days=today.weekday() + 2)
    one_week = datetime.timedelta(days=6)
    end_week = last_friday + one_week
    
    week_start_dates = formI_model.objects.all().order_by('-week_start')
    week_almost = week_start_dates[0]
    week = week_almost.week_start
    
    if week == last_friday:
        data = week_almost
        empty_form = formI_form()
        if request.method == "POST":
            form = formI_form(request.POST)
            A_valid = form.is_valid()
            if A_valid:
                A = request.POST
                
                return redirect('IncompleteForms')

    else:
        initial_data = {
            'week_start' : last_friday,
            'week_end' : end_week
        }
        data = formI_form()
        empty_form = formI_form(initial= initial_data)
        if request.method == "POST":
            form = formI_form(request.POST)
            A_valid = form.is_valid()
            if A_valid:
                form.save()

                return redirect('IncompleteForms')
        
    return render (request, "Daily/formI.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'empty': empty_form, 'week': week, 'last_friday': last_friday, 'week_almost': week_almost, 'end_week': end_week
    })

#----------------------------------------------------------------------FORM L---------------<
@lock
def formL(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    
    today = datetime.date.today()
    last_friday = today - datetime.timedelta(days=today.weekday() + 2)
    one_week = datetime.timedelta(days=6)
    end_week = last_friday + one_week
    
    week_start_dates = formL_model.objects.all().order_by('-week_start')
    week_almost = week_start_dates[0]
    week = week_almost.week_start
    
    if week == last_friday:
        data = week_almost
        empty_form = formL_form()
        if request.method == "POST":
            form = formL_form(request.POST)
            A_valid = form.is_valid()
            if A_valid:
                A = request.POST
                
                return redirect('IncompleteForms')

    else:
        initial_data = {
            'week_start' : last_friday,
            'week_end' : end_week
        }
        data = formL_form()
        empty_form = formL_form(initial= initial_data)
        if request.method == "POST":
            form = formL_form(request.POST)
            A_valid = form.is_valid()
            if A_valid:
                form.save()
                
                done = Forms.objects.filter(form='L')[0]
                done.submitted = True
                done.save()

                return redirect('IncompleteForms')
        
    return render (request, "Daily/formL.html", {
        "back": back, 'todays_log': todays_log, 'data': data, 'empty': empty_form, 'week': week, 'last_friday': last_friday, 'week_almost': week_almost, 'end_week': end_week
    })

#------------------------------------------------------------------------FORM M---------------<
@lock
def formM(request):
    daily_prof = daily_battery_profile_model.objects.all().order_by('-date_save')
    todays_log = daily_prof[0]
    full_name = request.user.get_full_name()
    cert_date = request.user.user_profile_model.cert_date
    
    initial_data = {
            'date' : todays_log.date_save,
            'observer' : full_name,
            'cert_date' : cert_date
    }
    form = formM_form(initial=initial_data)
    #submitted = False
   # if request.method == "POST":
   #     CReadings = FormCReadForm(request.POST)
   #     CData = SubFormC1(request.POST)
   #    A_valid = CReadings.is_valid()
   #     B_valid = CData.is_valid()
        #form.save()
        #return HttpResponseRedirect('./formC?submitted=True')
   #     if A_valid and B_valid:
   #         A = CData.save()
   #         B = CReadings.save(commit=False)
   #         B.form = A
   #         B.save()
   #         return HttpResponseRedirect('./formC?submitted=True')
   # else:
   #    form = SubFormC1
   #     read = FormCReadForm
   #     if 'submitted' in request.GET:
   #         submitted = True
    return render (request, "Daily/formM.html", {
        'now': todays_log, 'form': form,# 'read': read, 'submitted': submitted, "back": back
    })










































