from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Note
        #fields = '__all__'
        fields = ['id', 'title', 'content', 'user', 'username']