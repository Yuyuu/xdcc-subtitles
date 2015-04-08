from django.http import HttpResponse, JsonResponse
from babelfish import Language
import subliminal


def index(request):
    return HttpResponse("Subtitles index.")


def search(request):
    languages = {Language(language) for language in request.GET.get('l').split(',')}
    videos = {subliminal.Video.fromname(name) for name in request.GET.get('q').split(',')}
    links = subliminal.get_best_subtitles_links(videos, languages)
    return JsonResponse(links)