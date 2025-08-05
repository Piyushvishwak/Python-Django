from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
def my_view(request):
    data = {
        "message": "Hello, Mr. Piyush!",
        "status": "success"
    }
    return JsonResponse(data)

def list_view(request):
    data = [
        {"id": 1, "name": "Book A"},
        {"id": 2, "name": "Book B"}
    ]
    return JsonResponse(data, safe=False)

# def list_view(request):
#     data = [
#         {"id": 1, "name": "Book A"},
        # {"id": 2, "name": "Book B"}               won't work until safe != false
#     ]
#     return JsonResponse(data) 


def error_view(request):
    data = {"error": "Something went wrong"}
    return JsonResponse(data, status=400)

# def ajax_view(request):
#     if request.method == "POST":
#         return JsonResponse({"result": "Data saved successfully!"})


@csrf_exempt
def ajax_view(request):
    if request.method == "POST":
        return JsonResponse({"result": "Post request received successfully!"})
    return JsonResponse({"error": "Only POST requests allowed"}, status=405)

def ajax_test_page(request):
    return render(request, 'ajax_post.html')