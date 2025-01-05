from django.shortcuts import render

# Create your views here.

class shab_class(TemplateView):
    template_name = 'class_template.html'


def shab_func(request):
    return render(request, 'func_template.html')

