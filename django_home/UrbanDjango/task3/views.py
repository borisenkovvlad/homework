from django.shortcuts import render


def shab_class(request):
    return render(request, 'index1.html')


def shab_func(request):
    return render(request, 'index2.html')