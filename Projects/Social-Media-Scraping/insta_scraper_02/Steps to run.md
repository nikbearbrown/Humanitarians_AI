# Installation
## first create a virtual env
```
python -m venv virtual
source virtual/bin/activate

```

## For Apple silicon first install torch
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

## Then install other requirements
pip install -r requirements.txt

## Install Playwright browsers
python -m playwright install

# Running locally

```
python ai_scrapper.py username -n 10
```
- here ai_scraper.py is the script for scrapping and performs requires analysis
- username is the handle on the instagram account 
- 10 represents the number of post you want to scrape, it will do 12 posts by default

example run 
```
 python ai_scrapper.py aquaticbrewing -n 10
```
## Output
excel file with columns: userhandle, date, image_path, screenshot_path, likes, original_caption, image_context, caption_summary, keywords

