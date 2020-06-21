#!/usr/bin/python
import  requests
import argparse
import os
from requests_html import HTML,HTMLSession

'''
Credits : 
Genius Api(https://genius.com/developers)
Genius Website (https://genius.com/)
'''

def main():
    #Getting command line arguments
    parse = argparse.ArgumentParser(prog="lyrics.py",usage='%(prog)s [Artist Name] [Song Name]')
    parse.add_argument("Artist_and_Song_name",nargs='+',help="Get the names of the song and artist")
    args = parse.parse_args()

    #Setting artist name and song
    artist_and_song = ' '.join(args.Artist_and_Song_name)

    #Setting the url for request
    base_url = 'https://api.genius.com' 
    access_token = os.environ.get('GENIUS_ACCESS_TOKEN') 
    param= {'q':artist_and_song}
    path = '/search'
    token = 'Bearer '+access_token
    header = {'Authorization': token}

    request = requests.get(base_url+path, params=param, headers=header)

    #Checking Request Status
    if(request.ok):

        r_dict = request.json()
    else:
        print("Bad Request")

    #Getting the title of the song and genius lyrics url
    response = r_dict['response']['hits'][0]['result']
    title = response['full_title']
    url = response['url']
    print(title)
    print(url)

    #Setting up requests_html library for scraping the website
    session = HTMLSession()
    r = session.get(url)


    #Getting the first html element containing  a <p> tag
    song_body = r.html.find("p",first=True).text
    print(song_body)


if __name__ == "__main__":
    main()



