from django.contrib.auth.models import User, Group

from rest_framework import serializers

from tutorial.snippets.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')