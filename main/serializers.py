from rest_framework import serializers

from main.models import Board, Card, Task, Favourite


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('owner',)

    def create(self, validated_data):
        validated_data['owner_id'] = self.context.get('request').user.id
        return Board.objects.create(**validated_data)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
