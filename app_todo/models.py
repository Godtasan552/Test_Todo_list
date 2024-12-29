from django.db import models

# Create your models here.
class Todoitem(models.Model):
    title = models.CharField(max_length=255) # ชื่อ title
    description = models.TextField(blank=True) 
    completed = models.BooleanField(default=False) #สถานะว่าทำเสร็จหรือยัง
    created_at = models.DateTimeField(auto_now_add=True)#วันที่สร้าง
    updated_at = models.DateTimeField(auto_now=True) # วันที่แก้ไขล่าสุด
    
    def __str__(self):
        return self.title # แสดงชื่อ title ใน Admin Panel