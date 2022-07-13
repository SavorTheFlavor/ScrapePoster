<h1>SrapePoster</h1>
A Python program made to automatically scrape videos from various different sources, edit them with FFMPEG and post them onto a platform such as YouTube or Instagram. Currently a W.I.P and is only built with Linux in mind for now.
<hr>
<h2>TODO:</h2>

- [x] General video compiling
- [x] Reddit video scraping
- [ ] YouTube posting
- [ ] Instagram posting
- [ ] Windows compatibility
<hr>
<h2>How to use:</h2>

1. Set preferred settings through changing variables in `config.py` , such as the amount of videos you want to compile into 1 file, intro/outro, video title, subreddit source, etc.

2. Run `main.py` , then wait for the videos to be scraped and compiled. once finished, a single file with the name of the `title` variable in `config.py` will show up in the content folder, and the program will stop.