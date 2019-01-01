from django.shortcuts import render, redirect,get_object_or_404

from .models import Todo
# Create your views here.
def index(request):
    all_todos = Todo.objects
    print('---',Todo.objects)
    return render(request,'todos/index.html',{'todos':all_todos})

def new(request):
    if request.method == "POST":
        print("request: ",(request.POST.get('is_completed', '')=='on'))
        todo = Todo.objects.create(subject=request.POST["subject"],body=request.POST["body"],is_completed=(request.POST.get('is_completed', False)=='on') )
        print(vars(todo))

        # リダイレクトする処理を追記
        # 第二引数には新しく作成した記事の主キーを渡す
        return redirect(show,todo.pk)

    return render(request,'todos/new.html')
    
def show(request,todo_id):
    detailtodo = get_object_or_404(Todo, pk=todo_id)
    return render(request,'todos/show.html',{'todo':detailtodo})
    

def edit(request,todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "POST":
        
        todo.subject = request.POST["subject"]
        todo.body = request.POST["body"]
        todo.is_completed = (request.POST.get('is_completed', False) == "on")
        print('-----------------------')
        print(vars(todo))
        todo.save()
        
        # todo = Todo.objects.create(subject=request.POST["subject"],body=request.POST["body"],is_completed=(request.POST.get('is_completed', '')=='on') )
        print(vars(todo))

        return redirect(show,todo.id)
    return render(request,'todos/edit.html',{"todo":todo})
    
def delete(request,todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect(index)
    
    