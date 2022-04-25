from django.shortcuts import render


def index(request):
    '''
    View to return the inex page
    '''
    return render(request, 'home/index.html')
