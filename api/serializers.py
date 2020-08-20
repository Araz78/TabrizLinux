from rest_framework import serializers


class SingleArticleSerializer(serializers.Serializer):
    title       = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=30)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    publish     = serializers.DateTimeField(required=True, allow_null=False)
    is_special  = serializers.BooleanField(required=True, allow_null=False)
