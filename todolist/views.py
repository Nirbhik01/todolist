from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

def Home(request):
    return render(request, "todolist/homepage.html")

def get_tasks_all(request):
    tasks = Task.objects.all().values("task_text", "task_label", "task_status","due_date")
    
    return JsonResponse(list(tasks), safe=False)

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task_text = data.get("task_text")
            task_label = data.get("task_label")
            task_status = data.get("task_status")
            task_due_date = data.get("due_date") 

            task = Task.objects.create(
                task_text=task_text,
                task_label=task_label,
                task_status=task_status,
                due_date=task_due_date if task_due_date else None
            )
            return JsonResponse({"success": True, "message": "Task added successfully."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return JsonResponse({"success": False, "message": "Invalid request method."})


def get_tasks(request):
    label = request.GET.get('label')
    status = request.GET.get('status')
    due_date = request.GET.get('due_date')
    print(label, status, due_date)
    tasks = Task.objects.all()
    print(label, status, due_date)
    if label:
        tasks = tasks.filter(task_label=label)
    if status:
        tasks = tasks.filter(task_status=status)
    if due_date:
        tasks = tasks.filter(due_date=due_date)

    tasks_data = tasks.values('id', 'task_text', 'task_label', 'task_status','due_date')
    return JsonResponse(list(tasks_data), safe=False)

@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({"success": True, "message": "Task deleted."})
        except Task.DoesNotExist:
            return JsonResponse({"success": False, "message": "Task not found."})
    return JsonResponse({"success": False, "message": "Invalid request method."})