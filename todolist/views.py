from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Task,User
from django.views.decorators.csrf import csrf_exempt
import json

def login_page(request):
    return render(request, "todolist/login.html")

def register_page(request):
    return render(request, "todolist/register.html")



@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already taken"})

        user = User(username=username)
        user.set_password(password)
        user.save()

        return JsonResponse({"success": True, "message": "User registered successfully"})

    return JsonResponse({"success": False, "message": "Invalid request"})

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                request.session["user_id"] = user.user_id
                return JsonResponse({"success": True, "message": "Login successful"})
            else:
                return JsonResponse({"success": False, "message": "Incorrect password"})
        except User.DoesNotExist:
            return JsonResponse({"success": False, "message": "User not found"})

    return JsonResponse({"success": False, "message": "Invalid request"})

def logout_user(request):
    request.session.flush()
    return redirect("todolist:login")

def Home(request):
    if not request.session.get("user_id"):
        
        return redirect("todolist:login")
    return render(request, "todolist/homepage.html",{"user_name": User.objects.get(user_id=request.session["user_id"]).username})

def get_tasks_all(request):
    user=request.session.get("user_id")
    user=User.objects.get(user_id=user)
    # select the task of the user stored in session
    tasks = Task.objects.filter(user_task=user).values("id","task_text","task_description", "task_label", "task_status","due_date")
    return JsonResponse(list(tasks), safe=False)

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        try:
            user=request.session.get("user_id")
            user=User.objects.get(user_id=user)
            data = json.loads(request.body)
            task_text = data.get("task_text")
            task_description = data.get("task_description")
            task_label = data.get("task_label")
            task_status = data.get("task_status")
            task_due_date = data.get("due_date") 

            task = Task.objects.create(
                user_task=user,
                task_text=task_text,
                task_description=task_description,
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
    
    tasks = Task.objects.all()
    
    if label:
        tasks = tasks.filter(task_label=label)
    if status:
        tasks = tasks.filter(task_status=status)
    if due_date:
        tasks = tasks.filter(due_date=due_date)

    # tasks_data = tasks.values('id', 'task_text', 'task_description','task_label', 'task_status','due_date')
    # select the task of the user stored in session
    tasks_data=tasks.filter(user_task=request.session.get("user_id")).values('id', 'task_text', 'task_description','task_label', 'task_status','due_date')
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


@csrf_exempt
def edit_task(request, task_id):
    if request.method == "PUT":
        try:
            task = Task.objects.get(id=task_id)
            
            # select the task of the user stored in session
            user=request.session.get("user_id")
            user=User.objects.get(user_id = user)
            task = Task.objects.filter(user_task=user).get(id=task_id)
            
            data = json.loads(request.body)

            task.task_text = data.get("task_text", task.task_text)
            task.task_description = data.get("task_description", task.task_description)
            task.task_label = data.get("task_label", task.task_label)
            task.task_status = data.get("task_status", task.task_status)
            task.due_date = data.get("due_date", task.due_date)

            task.save()
            return JsonResponse({"success": True, "message": "Task updated successfully."})
        except Task.DoesNotExist:
            return JsonResponse({"success": False, "message": "Task not found."})
    return JsonResponse({"success": False, "message": "Invalid request method."})
