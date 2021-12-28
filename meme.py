"""Meme.py facilitates api to call the meme engine that generates the meme."""
import argparse
import os
import random

from MemeGenerator import MemeEngine
from QuoteEngine import QuoteModel, Ingestor


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quo = Ingestor.parse(f)
            quotes.extend(quo)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


def make_args() -> argparse.ArgumentParser:
    """Make argument parser."""
    parser = argparse.ArgumentParser(description='Generate meme.')
    parser.add_argument('--body', type=str, help='Quote body.')
    parser.add_argument('--author', type=str, help='Quote author.')
    parser.add_argument('--path', type=str, help='Image path.')
    return parser


if __name__ == "__main__":
    args = make_args().parse_args()
    print(generate_meme(args.path, args.body, args.author))
