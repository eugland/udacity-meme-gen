# Meme Generator

This is a web app that generate meme of a picture and a quote from an author. The user may specify the size of the 
image. 

## Setup
1. Get python 3.8.10
2. install pdftotext tool via `sudo apt-get update && sudo apt-get install -y poppler-utils`
3. install python virtual enrivonment: 
    `apt install python3-venv`
4. init a virtual env: `python -m venv venv`
5. install python depenecies via the requirement.txt file. `pip install -r requirements.txt`
6. run the web app: `python app.py`

## Project Structure
The project has mostly 2 modules and 2 controling files:
- Quote Engine 
- Meme Generator
- Meme.py - meme creator Api
- app.py - flask app

### Quote Engine
This module contains all functions, strategy objects and encapsulation with third party libraries
for parsing different types of data format, namely csv, docx, pdf, and txt, and assigning them to 
a `QuoteModal`

**quote_modal**: stores quote and author pair

**Intestor_interface.py**: has a parse abstract method that needs to be implmented by subclass, has a can parse 
to determine if a data is parsable.
- `CSVIngestor`: parse csv file
- `DocxIngestor`: parse docx file
- `TxtIngestor`: parse txt file
- `PDFIngestor`: parse pdf

**ingestor.py**: uses all ingestor above for parsing

### Meme Generator
the meme generator create a meme based on picture and quote. 

```
m = MemeGenerator
m.make_meme(img_path, text, author, width)
```

### meme.py API
```python

Generate meme.

- h         help
--body      quote body
--author    quote author
--path      image path
```

### flask app
This serves the app at localhost:5000 upon running
- `/`: the homepage serves a randomly generated meme
- `/create`: lets user create a meme with custome img, quote, and author
