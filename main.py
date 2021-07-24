from dotenv import load_dotenv
load_dotenv()

import time
import traceback
import asyncio

from twitter_api import *
from helper import *

    
class Listener(tweepy.StreamListener):
    def on_status(self, status):
        
        if status.user.screen_name == "TextSynth":
            return

        
        async def container():
            attempt = 0

            while True:
                try:
                    print("attempting to reply...")
                    await reply(twitter, status)
                    break
                except:
                    traceback.print_exc()
                    attempt += 1

                    if attempt > 10:
                        print("error max attempt reached...")
                        break
        
        asyncio.get_event_loop().run_until_complete(container()))

        for status in tweepy.Cursor(twitter.home_timeline).items(20):
            asyncio.get_event_loop().run_until_complete(reply(twitter, status))
            time.sleep(10)


    def on_error(self, status_code):
        if status_code == 420:
            print("ahhhh")
            time.sleep(20)
            return False
        
        print(status_code)

stream = tweepy.Stream(auth, Listener())


while True:
    try:
        print("bot starting...")
        stream.filter(track=["@TextSynth"])
            
    except Exception as e:
        traceback.print_exc()
        time.sleep(10)
