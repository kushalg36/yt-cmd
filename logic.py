from seleniumDriver import new_driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from apiclient.discovery import build
import os
import time

class logic:

    def __init__(self):
        self.actions = None
        self.driver = new_driver()
        self.url = 'https://www.google.com'
        self.driver.get(self.url)
        self.video_id=''
        self.api_key = os.environ.get('yt_api')
        self.youtube = build('youtube','v3',developerKey=self.api_key)

    def search(self, query):
        """
        Search function
        """
        # api_key = os.environ.get('yt_api')
        # youtube = build('youtube','v3',developerKey=api_key)
        youtube = self.youtube
        request_for_search = youtube.search().list(
            part = "snippet",
            maxResults = '1',
            q = query
        )
        response = request_for_search.execute()
        video_id = response['items'][0]['id']['videoId']
        self.video_id=video_id
        self.url = "https://www.youtube.com/watch?v=" + video_id
        self.driver.get(self.url)
        button = self.driver.find_element_by_css_selector(".ytp-play-button.ytp-button")
        coordinates = button.location_once_scrolled_into_view
        button.click()
        return True

    def video_info(self):
        """
        Returns song_title and channel_name
        """
        youtube = self.youtube
        request_for_video = youtube.videos().list(
            part="snippet,contentDetails",
            id=self.video_id
        )
        response = request_for_video.execute()

        video_title = response['items'][0]['snippet']['title']
        video_channel = response['items'][0]['snippet']['channelTitle']
        info = str('Playing video '+ video_title +' by '+ video_channel) 
        return info

    def action(self,button):
        """
        ActionChain initialization
        """
        self.actions = ActionChains(self.driver)
        self.actions.send_keys(button)
        self.actions.perform()
        self.actions = None

    def next(self):
        """
        Play next song in the suggestion
        """
        # button = Keys.LEFT_SHIFT,'n'
        # self.action(button)
        button = self.driver.find_element_by_css_selector(".ytp-next-button.ytp-button")
        button.click()

    def play_pause(self):
        """
        Play/Pause your song 
        """
        # button = 'k'
        # self.action(button)
        button = self.driver.find_element_by_css_selector(".ytp-play-button.ytp-button")
        button.click()

    def seek_forward(self):
        """
        Seek forward 5 seconds
        """
        button = Keys.ARROW_RIGHT
        self.action(button)

    def seek_backward(self):
        """
        Seek backward 5 seconds
        """
        button = Keys.ARROW_LEFT
        self.action(button)

    def close(self):
        """
        Close the browser
        """
        self.driver.quit()