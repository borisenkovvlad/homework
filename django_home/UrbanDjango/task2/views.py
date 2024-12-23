from django.shortcuts import render

# Create your views here.

class shab_class(TemplateView):
    template_name = 'index1.html'


def shab_func(request):
    return render(request, 'index2.html')

