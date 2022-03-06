from django.views.generic import View
from django.shortcuts import render
from matplotlib.style import context

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'index.html', context)