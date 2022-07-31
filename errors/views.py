from django.shortcuts import render

# Create your views here.
def error_500(request):
    data = {
        'status':"500 Internal Server Error"
    }
    return render(request, 'errors/error.html', data)

def error_404(request, exception):
    data = {
        'status':"500 Internal Server Error",
        "exception":exception
    }

    return render(request, 'errors/error.html', data)