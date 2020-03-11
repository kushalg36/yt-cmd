from apiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 

api_key = 'AIzaSyAPdA0K_BWOMddIl3iHUl39UNeI4qXOsJk'

youtube = build('youtube','v3',developerKey=api_key)

search = input('Enter the song you want to play==> ')

request_for_serach = youtube.search().list(
    part = "snippet",
    maxResults = '1',
    q = search
)

response = request_for_serach.execute()
video_id = response['items'][0]['id']['videoId']

request_for_video = youtube.videos().list(
        part="snippet,contentDetails",
        id=video_id
    )

response = request_for_video.execute()

video_duration = response['items'][0]['contentDetails']['duration']
video_title = response['items'][0]['snippet']['title']
video_channel = response['items'][0]['snippet']['channelTitle']

print('Playing video '+ video_title +' by '+ video_channel)

duration_ms = (int(video_duration[ video_duration.find("M")-1 ]) * 60000 ) + (int(video_duration[video_duration.find("M")+1]) * 10000 ) + (int(video_duration[video_duration.find("S")-1]) * 1000 )


options = Options()
options.headless = True

driver = webdriver.Firefox(options=options) 
driver.get("https://www.youtube.com/watch?v=" + video_id)
button = driver.find_element_by_class_name('ytp-play-button')#ytp-button
button.click()

# print(duration_ms)

time.sleep(duration_ms/1000)
# print('Over')

driver.quit()