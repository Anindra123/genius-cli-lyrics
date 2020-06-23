#!/usr/bin/python
import  requests
import argparse
import os
import sys
import mpv
import curses
from youtube_search import YoutubeSearch
from requests_html import HTML,HTMLSession

'''
Credits : 
Genius Api(https://genius.com/developers)
Genius Website (https://genius.com/)
'''

def get_artist_and_song():
    #Getting command line arguments
    parse = argparse.ArgumentParser(prog="lyrics.py",usage='%(prog)s [Artist Name] [Song Name]')
    parse.add_argument("Artist_and_Song_name",nargs='+',help="Get the names of the song and artist")
    args = parse.parse_args()

    #Setting artist name and song
    artist_and_song = ' '.join(args.Artist_and_Song_name)
    return artist_and_song

def get_genius_artist_dict(artistAndsong,url):
    
    access_token = os.environ.get('GENIUS_ACCESS_TOKEN') 
    param= {'q':artistAndsong}
    path = '/search'
    token = 'Bearer '+access_token
    header = {'Authorization': token}
    return requests.get(url+path, params=param, headers=header)    
       
def get_result(get_response):
    try:
        return get_response.json()['response']['hits'][0]['result']
    except IndexError:
        print("Bad Request or not a song")
        sys.exit(1)

def scrape_lyrics(url):
    #Setting up requests_html library for scraping the website
    session = HTMLSession()
    r = session.get(url)

    #Getting the first html element containing  a <p> tag
    song_body = r.html.find("p",first=True).text
    
    return song_body
        
def get_yt_link(artistAndsong,url):
    try:
        link = YoutubeSearch(artistAndsong,max_results=10).to_dict()
        return url + link[1]['link']
    except IndexError:
        print("Couldn't return link. Please try again")
        sys.exit(1)


def play_mpv(url):
    player = mpv.MPV(log_handler=print,ytdl=True,vid=False,input_default_bindings=True)
    player.play(url)
    player.wait_for_playback()
            
def main():
    #Setting necessary urls 
    genius_api_url = 'https://api.genius.com'
    youtube_url = 'https://www.youtube.com'


    #Getting the artist name and song name
    artist_and_song_name = get_artist_and_song()

    #Getting response from genius api
    response = get_genius_artist_dict(artist_and_song_name,genius_api_url)

    if(response != None and response.ok):
    #Getting the dictonary for song and artist
        result = get_result(response) 
    
    #Printng the title
        print(result['full_title'])

    #Getting the url for scraping lyrics
        lyrics_url = result['url']

    #Getting and Printing the lyrics
        lyrics = scrape_lyrics(lyrics_url)

        print(lyrics)

    #Getting the youtube link for the song
        yt_link  = get_yt_link(artist_and_song_name,youtube_url)
    #Playing the song using mpv library for python
        play_mpv(yt_link)


if __name__ == "__main__":
    main()



