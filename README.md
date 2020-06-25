# muly-cli

A python cli script that uses [Genius Api](https://genius.com/developers) and [requests_html](https://requests-html.kennethreitz.org/) library for scraping to get the lyrics of a song and uses [mpv](https://mpv.io/) to play music on the command line


you need an authoriztion key which can be get through creating a free account at [Genius](https://genius.com/) then setting it as an environment variable on your ```.bashrc``` or ```.zshrc``` file like

``````
export GENIUS_ACCESS_TOKEN="your token"

``````

## Build

``````
clone the repository
cd muly-cli/
chmod u+x muly.py

``````

Then run the script.To get the desried lyrics of a song  
``````
./muly.py -l Artist_name Song_name

``````

To play a song

``````
./muly.py -m Artist_name Song_name

``````
This will open an mpv instance on the command line to exit that just press "q" on keyboard

## Issues

There are still some bugs and issues with this script i haven't figured out yet since i am still a novice programmer and my experience with web-scraping is rather poor.Since i am scraping big javascript heavy sites often the scraping returns incomplete result.
``````
Example :

For lyrics

❯ /muly.py -l Kevin Abstract Echo
Now Playing Echo by Kevin Abstract
Produced by

``````
It will get stuck at that and for playing the song you will get a message saying ```Couldn't return link please try again``` which is an exception i wrote just to clarify the bug. The workaround i got with this issue is just to run the command two or three times and it would return the result.
But i know this is not an optimal solution but since i made this script as a hobby project i am not looking that deep for solution even though i tried a lot of fixes and none of them worked for me. So if any one of you going through the project know the solution or want to help me to further code and want to help me to learn i will gladly accept it.

## Dependecies

* [requests_html](https://requests-html.kennethreitz.org/)
* [argparse](https://requests-html.kennethreitz.org/)
* [youtube-search](https://pypi.org/project/youtube-search/)
* Python 
* pip
* [mpv](https://mpv.io/)
* A notification server running for using ```Notify-Send``` command

## Credits
* Genius Api(https://genius.com/developers)
* Genius Website (https://genius.com/)
