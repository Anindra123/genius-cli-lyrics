#!/usr/bin/python
import  requests
import argparse
import os
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

def get_genius_artist_dict(artist_and_song,url):
    access_token = os.environ.get('GENIUS_ACCESS_TOKEN') 
    param= {'q':artist_and_song}
    path = '/search'
    token = 'Bearer '+access_token
    header = {'Authorization': token}

    return requests.get(url+path, params=param, headers=header)    

def get_result(get_response):
    if(get_response.ok):
        return get_response.json()['response']['hits'][0]['result']

    else:
        "Bad Request or Not a Song"
def scrape_lyrics(url):
    #Setting up requests_html library for scraping the website
    session = HTMLSession()
    r = session.get(url)

    #Getting the first html element containing  a <p> tag
    song_body = r.html.find("p",first=True).text
    
    return song_body
        


def main():
    #Setting necessary urls 
    genius_api_url = 'https://api.genius.com'
    #youtube_url = 'https://www.youtube.com'


    #Getting the artist name and song name
    artist_and_song_name = get_artist_and_song()

    #Getting response from genius api
    response = get_genius_artist_dict(artist_and_song_name,genius_api_url)

    #Getting the dictonary for song and artist
    result = get_result(response) 
    
    #Printng the title
    print(result['full_title'])

    #Getting the url for scraping lyrics
    lyrics_url = result['url']

    #Getting and Printing the lyrics
    lyrics = scrape_lyrics(lyrics_url)

    print(lyrics)
            

    #results = YoutubeSearch(artist_and_song,max_results=10).to_dict()

        

if __name__ == "__main__":
    main()



