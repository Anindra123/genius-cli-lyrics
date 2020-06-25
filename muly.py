#!/usr/bin/python
import requests
import argparse
import os
import sys
from youtube_search import YoutubeSearch
from requests_html import HTML,HTMLSession

'''
Credits : 
Genius Api(https://genius.com/developers)
Genius Website (https://genius.com/)
'''


def get_args():
    #Getting command line arguments
    parse = argparse.ArgumentParser(prog="lyrics.py",usage='%(prog)s [Artist Name] [Song Name]')
    parse.add_argument("Artist_and_Song_name",nargs='+',help="Get the names of the song and artist")
    parse.add_argument("-m",help="Play music in mpv")
    parse.add_argument("-l",help="Get the lyrics of a song")
    args = parse.parse_args()

    #Setting artist name and song
    return args

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

def play_mpv(url,title):
    os.system('notify-send \'{}\''.format(title)+';mpv --no-video '+url)

            
def main():
    #Setting necessary urls 
    genius_api_url = 'https://api.genius.com'
    youtube_url = 'https://www.youtube.com'


    #Getting command line arguments 
    args = get_args()
    if(args.l):
        artist_and_song_name =' '.join(args.Artist_and_Song_name)

        #Getting the response
        response = get_genius_artist_dict(artist_and_song_name,genius_api_url)
        
        #Getting the dictonary for song and artist
        result = get_result(response)
        
        #Printing the title
        print(result['full_title'])
        
        #Getting the url for scraping lyrics
        lyrics_url = result['url']
        
        #Getting and Printing the lyrics
        lyrics = scrape_lyrics(lyrics_url)

        print(lyrics)

    elif(args.m):
        artist_and_song_name =' '.join(args.Artist_and_Song_name)

        #Getting the response
        response = get_genius_artist_dict(artist_and_song_name,genius_api_url)
        
        #Getting the dictonary for song and artist
        result = get_result(response)

        #Notify
        full_title = "Now Playing " + result['full_title']
        print(full_title)

        #Getting the youtube link for the song
        yt_link  = get_yt_link(artist_and_song_name,youtube_url)
        
        #Playing the song using mpv 
        play_mpv(yt_link,full_title)

   
if __name__ == "__main__":
    main()



