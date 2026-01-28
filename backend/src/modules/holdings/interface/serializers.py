from rest_framework import serializers

class PageOut(serializers.Serializer):
    slug = serializers.CharField()
    title = serializers.CharField()
    body = serializers.CharField()
    updated_at = serializers.DateTimeField()
