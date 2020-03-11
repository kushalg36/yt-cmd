from apiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

api_key = ''

youtube = build('youtube','v3',developerKey=api_key)

request = youtube.search().list(
    part = "snippet",
    maxResults = '1',
    q = 'homicide logic'
)

response = request.execute()

video_id = response['items'][0]['id']['videoId']

# print(response['contentDetails']['duration'])

request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )

response = request.execute()

# print(response['contentDetails']['duration'])

video_duration =  response['items'][0]['contentDetails']['duration']

print(video_duration)

duration_ms = (int(video_duration[ video_duration.find("M")-1 ]) * 60000 ) + (int(video_duration[video_duration.find("M")+1]) * 10000 ) + (int(video_duration[video_duration.find("S")-1]) * 1000 )

print(duration_ms)