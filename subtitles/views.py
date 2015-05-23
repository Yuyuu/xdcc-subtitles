from django.http import HttpResponse, JsonResponse
from babelfish import Language
import subliminal


def index(request):
    return HttpResponse("Subtitles index.")


def download(request):
    language_query = request.GET.get('l')
    video_query = request.GET.get('q')

    if language_query is None or video_query is None:
        response = JsonResponse({'errors': [{'message': 'MISSING_PACK_OR_LANGUAGE'}]})
        response.status_code = 400
        return response

    language = Language(language_query)
    video = subliminal.Video.fromname(video_query)

    subtitles = subliminal.download_best_subtitles({video}, {language})
    if len(subtitles[video]) == 0:
        response = HttpResponse("No subtitles found for %s" % video.name)
    else:
        content = subtitles[video][0].content
        response = HttpResponse(content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s.srt' % basename(video.name)

    return response


def basename(filename):
    dot_index = filename.rfind('.')
    return filename[:dot_index] if dot_index > 0 else filename