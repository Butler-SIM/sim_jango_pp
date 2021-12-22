from django.http import JsonResponse


def error404(request, exception=None):
    return JsonResponse({
        'code': "E0404",
        'message': "주소(URL)가 올바르지 않습니다.",
        'data': None
    })


def error403(request, exception=None):
    return JsonResponse({
        'code': "E0403",
        'message': "접근 권한이 없습니다.",
        'data': None
    })


def error400(request, exception=None):
    return JsonResponse({
        'code': "E0400",
        'message': "요청(Request)이 올바르지 않습니다.",
        'data': None
    })


def error500(request, exception=None):
    return JsonResponse({
        'code': "E0500",
        'message': "서버(Server)에 문제가 있습니다.",
        'data': None
    })