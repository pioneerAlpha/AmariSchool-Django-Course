from rest_framework import serializers, validators
from .models import *

# class ListSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(required=True, allow_blank=True, max_length=100)
#     description=serializers.CharField()
    
#     def create(self, validate_data):
#         return List.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.name=validate_data.get('name', instance.name)
#         instance.description=validate_data.get('description', instance.description)
#         instance.save()
#         return instance
    
    
    
# class ListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = List
#         fields = '__all__'
    
#     # def validate_name(self, value):
#     #     if len(value)<5:
#     #         raise serializers.ValidationError('Name cannot be less than 5')
#     #     return value
    
#     # def validate(self, data):
        
#     #     name=data.get('name')
        
#     #     if List.objects.filter(name=name).exists():
#     #         raise serializers.ValidationError('Name is already in database')
#     #     return data
    
#         validators=[
#             validators.UniqueTogetherValidator(
#                 queryset=List.objects.all(),
#                 fields=['name', 'description'],
#                 message="Name and description already existed"
#             ),
#         ]
    
        
    

        
        
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album