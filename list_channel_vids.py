import argparse
import os
from datetime import datetime
from googleapiclient.discovery import build

def get_youtube_service(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def get_all_videos(youtube, channel_id):
    videos = []
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )
    while request:
        response = request.execute()
        for item in response['items']:
            if item['id']['kind'] == 'youtube#video':
                videos.append(item['id']['videoId'])
        request = youtube.search().list_next(request, response)
    return videos

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch all videos from a YouTube channel.')
    parser.add_argument('channel_id', help='The ID of the YouTube channel')
    args = parser.parse_args()

    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("Please set the YOUTUBE_API_KEY environment variable.")

    youtube = get_youtube_service(api_key)
    videos = get_all_videos(youtube, args.channel_id)
    for video_id in videos:
        print(f"https://www.youtube.com/watch?v={video_id}")

