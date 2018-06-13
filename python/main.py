import json

def hello(request):
    body = {
        "message": "Go Serverless  with py-cloud-fn! Your function executed successfully!",
        "input": request.json
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response