from rest_framework import serializers
from rest_framework.fields import SlugField

from todoForm.models import Todo_model, Validation_model
from rest_framework.validators import UniqueValidator
from rest_framework.validators import UniqueTogetherValidator


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_model
        fields = ('id', 'title', 'description', 'save')


class Todo_validationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation_model
        fields = ('id', 'username', 'password')


class Todo_unique(serializers.Serializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Todo_model.objects.all(),
                fields=['list', 'position']
            )
        ]

        slug = SlugField(
            max_length=100,
            validators=[UniqueValidator(queryset=Todo_model.objects.all())]
        )
