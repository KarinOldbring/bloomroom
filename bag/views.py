from django.shortcuts import render

def view_bag(request):
    """
    View to render bag page
    """
    return render(request, 'bag/bag.html')
