from django.shortcuts import render, redirect
from joblib import load

model = load('./Suicde_Model/suicide_prediction_model.joblib')


# Create your views here.

def home(request):
    return render(request, 'webpages/home.html')


def services(request):
    if request.method == 'POST':
        Sex = request.POST['Sex']
        Currently_Drink_Alcohol = request.POST['Currently_Drink_Alcohol']
        Really_Get_Drunk = request.POST['Really_Get_Drunk']
        Overwieght = request.POST['Overwieght']
        Use_Marijuana = request.POST['Use_Marijuana']
        Have_Understanding_Parents = request.POST['Have_Understanding_Parents']
        Missed_classes_without_permssion = request.POST['Missed_classes_without_permssion']
        Had_sexual_relation = request.POST['Had_sexual_relation']
        Smoke_cig_currently = request.POST['Smoke_cig_currently']
        Had_fights = request.POST['Had_fights']
        Bullied = request.POST['Bullied']
        Got_Seriously_injured = request.POST['Got_Seriously_injured']
        No_close_friends = request.POST['No_close_friends']
        y_pred = model.predict([[Sex, Currently_Drink_Alcohol, Really_Get_Drunk, Overwieght, Use_Marijuana, Have_Understanding_Parents, Missed_classes_without_permssion, Had_sexual_relation, Smoke_cig_currently, Had_fights, Bullied, Got_Seriously_injured, No_close_friends]])
        if y_pred[0] == 0:
            y_pred = "This person does not have suicidal thoughts!!"
        else:
            y_pred = "This person has suicidal thoughts!!"

        return render(request, 'webpages/services.html', {'result': y_pred})
    return render(request, 'webpages/services.html')


#

def about(request):
    return render(request, 'webpages/about.html')


def contact(request):
    return render(request, 'webpages/contact.html')
