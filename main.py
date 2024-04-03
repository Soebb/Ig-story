from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import os
USERNAME=os.environ.get("INSTAGRAM_USERNAME")
PASSWORD=os.environ.get("PASSWORD")
cl = Client()
cl.login(USERNAME, PASSWORD)
url = 'https://www.instagram.com/p/CX37ituIcyr/?igsh=OHBnN2ptYWxoOXQw'
media_pk = cl.media_pk_from_url(url)

media_path = cl.video_download(media_pk)
example = cl.user_info_by_username('san_a_01')
#hashtag = cl.hashtag_info('dhbastards')

cl.video_upload_to_story(
    media_path,
    #"Credits @example",
    mentions=[StoryMention(user=example)],
    #mentions=[StoryMention(user=example, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    #links=[StoryLink(webUri='https://github.com/subzeroid/instagrapi')],
    #hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
    medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)],
)
