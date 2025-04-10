from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
# from django.views.decorators.csrf import csrf_exempt
import json

def Home(request):
    return render(request, "todolist/homepage.html")

def get_tasks(request):
    tasks = Task.objects.all().values("task_text", "task_label", "task_status")
    return JsonResponse(list(tasks), safe=False)

# @csrf_exempt
def add_task(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task_text = data.get("task_text")
            task_label = data.get("task_label")
            task_status = data.get("task_status")

            task = Task.objects.create(
                task_text=task_text,
                task_label=task_label,
                task_status=task_status
            )
            return JsonResponse({"success": True, "message": "Task added successfully."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return JsonResponse({"success": False, "message": "Invalid request method."})


def get_tasks(request):
    label = request.GET.get('label')
    status = request.GET.get('status')

    tasks = Task.objects.all()

    if label:
        tasks = tasks.filter(task_label=label)
    if status:
        tasks = tasks.filter(task_status=status)

    tasks_data = tasks.values('id', 'task_text', 'task_label', 'task_status')
    return JsonResponse(list(tasks_data), safe=False)

# @csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({"success": True, "message": "Task deleted."})
        except Task.DoesNotExist:
            return JsonResponse({"success": False, "message": "Task not found."})
    return JsonResponse({"success": False, "message": "Invalid request method."})