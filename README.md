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
    
**list-to-download.txt**
```
Avicii - Lord
Avicii - Sunset Jesus
Avocuddle - Fly me to the moon
Darude - Sandstorm
```

- Run `./download.sh`
    - It will download the songs and move them into the `Music` folder  
    
```
[user@computer Youtube-Music-Downloader] $ ./download.sh

Youtube Music Downloader

1. Avicii - Lord (Ft. Sandro Cavazza)
Downloading: Avicii - Lord (Ft. Sandro Cavazza).
Avicii - Lord (Ft. Sandro Cavazza)
  1,024.0 Bytes [2.84%] received. Rate: [   0 KB/s].  ETA  3,072.0 Bytes [8.51%] received. Rate: [   0 KB/s].  ETA  7,168.0 Bytes [19.86%] received. Rate: [   0 KB/s].  ET  15,360.0 Bytes [42.55%] received. Rate: [ 964 KB/s].  E  31,744.0 Bytes [87.94%] received. Rate: [1811 KB/s].  E  36,097.0 Bytes [100.00%] received. Rate: [1812 KB/s].  ETA: [0 secs]    

Audio remuxed.

1. Avicii - Sunset Jesus (Lyric Video)
Downloading: Avicii - Sunset Jesus (Lyric Video).
Avicii - Sunset Jesus (Lyric Video)
  1,024.0 Bytes [0.02%] received. Rate: [ 818 KB/s].  ETA  3,072.0 Bytes [0.07%] received. Rate: [2342 KB/s].  ETA  7,168.0 Bytes [0.17%] received. Rate: [5302 KB/s].  ETA  15,360.0 Bytes [0.36%] received. Rate: [11001 KB/s].  E  31,744.0 Bytes [0.75%] received. Rate: [5057 KB/s].  ET  64,512.0 Bytes [1.53%] received. Rate: [4796 KB/s].  ET  130,048.0 Bytes [3.09%] received. Rate: [6757 KB/s].  E  261,120.0 Bytes [6.20%] received. Rate: [9256 KB/s].  E  523,264.0 Bytes [12.42%] received. Rate: [12063 KB/s].   1,047,552.0 Bytes [24.87%] received. Rate: [17159 KB/s]  2,096,128.0 Bytes [49.76%] received. Rate: [19571 KB/s]  4,193,280.0 Bytes [99.54%] received. Rate: [26071 KB/s]  4,212,614.0 Bytes [100.00%] received. Rate: [25318 KB/s].  ETA: [0 secs]    

Audio remuxed.

1. Avocuddle - Fly Me To The Moon
Downloading: Avocuddle - Fly Me To The Moon.
Avocuddle - Fly Me To The Moon
  1,024.0 Bytes [0.04%] received. Rate: [ 652 KB/s].  ETA  3,072.0 Bytes [0.11%] received. Rate: [1843 KB/s].  ETA  7,168.0 Bytes [0.26%] received. Rate: [4140 KB/s].  ETA  15,360.0 Bytes [0.55%] received. Rate: [8509 KB/s].  ET  31,744.0 Bytes [1.13%] received. Rate: [4947 KB/s].  ET  64,512.0 Bytes [2.30%] received. Rate: [5087 KB/s].  ET  130,048.0 Bytes [4.64%] received. Rate: [7026 KB/s].  E  261,120.0 Bytes [9.32%] received. Rate: [9739 KB/s].  E  523,264.0 Bytes [18.68%] received. Rate: [13638 KB/s].   1,047,552.0 Bytes [37.39%] received. Rate: [18806 KB/s]  2,096,128.0 Bytes [74.82%] received. Rate: [22670 KB/s]  2,801,497.0 Bytes [100.00%] received. Rate: [23168 KB/s].  ETA: [0 secs]    

Audio remuxed.

1. Darude - Sandstorm
Downloading: Darude - Sandstorm.
Darude - Sandstorm
  1,024.0 Bytes [0.03%] received. Rate: [ 748 KB/s].  ETA  3,072.0 Bytes [0.08%] received. Rate: [2092 KB/s].  ETA  7,168.0 Bytes [0.19%] received. Rate: [4659 KB/s].  ETA  15,360.0 Bytes [0.41%] received. Rate: [9491 KB/s].  ET  31,744.0 Bytes [0.84%] received. Rate: [3918 KB/s].  ET  64,512.0 Bytes [1.72%] received. Rate: [4568 KB/s].  ET  130,048.0 Bytes [3.46%] received. Rate: [5953 KB/s].  E  261,120.0 Bytes [6.94%] received. Rate: [9274 KB/s].  E  523,264.0 Bytes [13.91%] received. Rate: [12642 KB/s].   1,047,552.0 Bytes [27.85%] received. Rate: [17393 KB/s]  2,096,128.0 Bytes [55.73%] received. Rate: [23338 KB/s]  3,760,893.0 Bytes [100.00%] received. Rate: [25663 KB/s].  ETA: [0 secs]    

Audio remuxed.

[user@computer Youtube-Music-Downloader] $ ls Music/

'Avicii - Lord (Ft. Sandro Cavazza).m4a'
'Avicii - Sunset Jesus (Lyric Video).m4a'
'Avocuddle - Fly Me To The Moon.m4a'
'Darude - Sandstorm.m4a'
```

- Check `Downloader` if you miss some song or the program crashes/freezes without finishing
    - `ls Downloader/`
    - If you see some song `.m4a` here, just run `./move.sh` to move it to `Music` folder  
- Play the music with `./play.sh`
    - If you are not familiarized with cmus, just press `5`, move up and down with the arrows and play the song with `Enter`  

```
 Browser - /route/Youtube-Music-Downloader
 
 ../
 Avicii - Lord (Ft. Sandro Cavazza).m4a
 Avicii - Sunset Jesus (Lyric Video).m4a
 Avocuddle - Fly Me To The Moon.m4a
 Darude - Sandstorm.m4a






 . 00:00 - 00:00                 all from library | C
```

- Enjoy!
