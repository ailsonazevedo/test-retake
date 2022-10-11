from process.models import Process, Parts
from rest_framework import serializers

class PartsSerializer(serializers.Serializer):
    class Meta:
        model = Parts
        fields = ('name',)

    def create(self, validated_data):
        return Parts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ProcessSerializer(serializers.ModelSerializer):
    parts = PartsSerializer(many=True)
    class Meta:
        model = Process
        fields = ['id', 'number','judicialClass','topic','judge','parts','category']

    def create(self, validated_data):
        parts_data = validated_data.pop('parts')
        process = Process.objects.create(**validated_data)
        for part_data in parts_data:
            Parts.objects.create(process=process, **part_data)
        return process
