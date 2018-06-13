from cloudfn.http import handle_http_event, Response


def handle_http(req):
    result = str(req) + "happy jolly day"
    return Response(
    status_code=200,
    body={'key': 2,
          'reply': result},
    headers={'content-type': 'application/json'},
    )


handle_http_event(handle_http)