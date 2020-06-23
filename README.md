# muly-cli

A python cli script that uses [Genius Api](https://genius.com/developers) and [requests_html](https://requests-html.kennethreitz.org/) library for scraping to get the lyrics of a song and uses [python-mpv](https://github.com/jaseg/python-mpv) library to play music on the command line


you need an authoriztion key which can be get through creating a free account at [Genius](https://genius.com/) then setting it as an environment variable on your ```.bashrc``` or ```.zshrc``` file like

``````
export GENIUS_ACCESS_TOKEN="your token"

``````

## Build

``````
clone the repository
cd genius-lyrics-cli/
chmod u+x lyrics.py

``````

Then run the script to get the desried lyrics of a song on the command line

``````
./lyrics.py Artist_name Song_name

``````

## Dependecies

* [requests_html](https://requests-html.kennethreitz.org/)
* [argparse](https://requests-html.kennethreitz.org/)
* [python-mpv](https://github.com/jaseg/python-mpv)
* Python 
* pip

## Credits
* Genius Api(https://genius.com/developers)
* Genius Website (https://genius.com/)
* python-mpv (https://github.com/jaseg/python-mpv)
