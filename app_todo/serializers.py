from rest_framework import serializers
from.models import Todoitem

class TodoitemSerlier(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ('id','title','description','completed','create_at','updated_at')