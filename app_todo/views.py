from django.shortcuts import render, HttpResponse,redirect

from .models import Todoitem

# Create your views here.
def indexPage(request):
    if request.method =="POST": #ตรวจสอบว่าเป็นการส่ง ฟอร์มแบบ POST หรือไม่
        task = request.POST.get("task") # ดึงค่าจาก input ที่ name="task"
        if task: #ตรวจสอบว่ามีค่าหรือไม่
            Todoitem.objects.create(task=task) # สร้าง task ใหม่ในฐานข้อมูล
        return redirect("index") # กลับไปหน้า index
    todos = Todoitem.objects.all() #ดึงรายการทั้งหมดจากฐานข้อมูล
    return render(request, "index.html",{"todos":todos}) #ส้่งข้อมูล todos กลับไปยัง template

def wathtodoPage(request):
    return render(request, "wathtodo.html")

