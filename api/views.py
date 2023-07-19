from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video, Subtitle
from .serializers import SubtitleSerializer


@api_view(['POST'])
def save_subtitles(request):
    video_id = request.data['videoId']
    subtitles_data = request.data['subtitles']

    try:
        video = Video.objects.get(name=video_id)
    except Video.DoesNotExist:
        video = Video(name=video_id)
        video.save()
    Subtitle.objects.filter(video=video).delete()

    subtitles = [
        Subtitle(video=video, text=subtitle['text'], time=subtitle['time'])
        for subtitle in subtitles_data
    ]
    Subtitle.objects.bulk_create(subtitles)

    return Response({'message': 'Subtitles saved successfully.'})


@api_view(['GET'])
def get_subtitles(request, video_id):
    try:
        video = Video.objects.get(name=video_id)
    except Video.DoesNotExist:
        return Response({'message': 'Video not found.'}, status=404)

    subtitles = Subtitle.objects.filter(video=video).values('text', 'time')
    return Response({'subtitles': list(subtitles)})
