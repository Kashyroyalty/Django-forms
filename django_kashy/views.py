from django.shortcuts import render

from .form import UserReg


def reg(request):
    submit_button = request.POST.get("kashy")
    name = ''
    email = ''
    password = ''

    regform = UserReg(request.POST or None)
    if regform.is_valid():
        name = regform.cleaned_data.get("name")
        email = regform.cleaned_data.get("emeil")
        password = regform.cleaned_data.get("password")

    context = {'regform': regform, 'name': name, 'email': email, 'submit_button': submit_button}
    return render(request, 'register.html', context)
