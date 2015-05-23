from django.http import HttpResponse


def start(request):
    return HttpResponse("OK")


def stop(request):
    return HttpResponse("OK")


def health_check(request):
    return HttpResponse("OK")