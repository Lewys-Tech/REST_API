from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tittle = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()