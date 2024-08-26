from rest_framework import serializers

from todo_list.models import Task, ToDoList


class TaskSerializer(serializers.ModelSerializer):
    todo_list_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Task
        fields = "__all__"

    # def validate(self, data):
    #     request = self.context.get('request')
    #     method = request.method if request else None
        
    #     if method in ['POST', 'PUT', 'PATCH', 'DELETE']:
    #         if 'todo_list_id' not in data:
    #             raise serializers.ValidationError({
    #                 'todo_list_id': 'This field is required for {} requests.'.format(method)
    #             })        
    #     return data
    
    def create(self, validated_data):
        todo_list_id = validated_data.pop('todo_list_id')
        new_task = Task.objects.create(**validated_data)
        list_instance = ToDoList.objects.get(id=todo_list_id)
        list_instance.tasks.add(new_task)
        return new_task