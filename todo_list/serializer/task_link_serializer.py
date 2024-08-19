from rest_framework import serializers

from todo_list.models import TaskLink


class TaskLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLink
        fields = ["uuid"]

    def get_fields(self):
        fields = super(TaskLinkSerializer, self).get_fields()
        context = self.context
        if context.get("read_only", False):
            fields["uuid"] = serializers.UUIDField(read_only=True)
        else:
            fields["uuid"] = serializers.UUIDField(read_only=False)
        return fields
