# Youtube Music Downloader
- Write down the song titles in `list-to-download.txt` and the tool will download them from Youtube.

## Dependencies
- python3
    - `sudo apt-get install python3`  
- BeautifulSoup
    - `pip install beautifulsoup4`  
- cmus
    - `sudo apt-get install cmus`  

## Usage
- Open `list-to-download.txt` with your favorite text editor
- Write down song titles (one per line)
    - The more exact the title, the better
    - I recommend adding the artist for better searches  
- Run `./download.sh`
    - It will download the songs and move them into the `Music` folder  
- Check `Downloader` if you miss some song or the program crashes/freezes without finishing
    - `ls Downloader/`
    - If you see some song `.m4a` here, just run `./move.sh` to move it to `Music` folder  
- Play the music with `./play.sh`
    - If you are not familiarized with cmus, just press `5`, move up and down with the arrows and play the song with `Enter`  
- Enjoy!
