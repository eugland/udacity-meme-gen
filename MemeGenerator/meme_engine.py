"""Meme Engine file output the meme engine class."""
import os
import pathlib
import random
import textwrap


from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """An engine that generates memes from data."""

    def __init__(self, output_dir: str):
        """Meme Engine initializer."""
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    def load_image(self, img_path: str):
        """Load image from the supplied path."""
        return Image.open(img_path)

    def resize(self, img, width: int):
        """Resize the meme and according to supplied width."""
        ratio = img.size[1] / img.size[0] # get height to width ratio
        return img.resize((width, int(width * ratio)), Image.ANTIALIAS)

    def add_caption(self, img, text: str, author: str):
        """Add caption to a meme picture.

        Param:
            img,
            text,
            author

        Return:
            the Image object of meme after caption added
        """
        draw = ImageDraw.Draw(img)
        font_path = (pathlib.Path(__file__).parent.parent.absolute() / "fonts/arial.ttf")
        print(font_path)
        font = ImageFont.truetype(str(font_path), 40)
        img_width, _ = img.size

        if text and author:
            lines = textwrap.wrap(f'{text} - {author}', width=20)
        y_text = 0
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text(((img_width - line_width) / 2, y_text),
                      line,
                      font=font,
                      fill=(0, 0, 0),)
            y_text += line_height

        return img

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """Make meme from image path, text, and author.

        Arugments:
            img_path
            text
            author
            width - optional

        return:
            a path of saved meme
        """
        assert(text is not None and author is not None), "You need text and author to make a meme"

        img = self.load_image(img_path)
        img = self.resize(img, width)
        img = self.add_caption(img, text, author)

        original_name = img_path.split(".jpg")[0].split("/")[-1]
        save_path = os.path.join(self.output_dir, f'{original_name}_modified_{random.randint(0, 10000000)}.jpg')
        img.save(save_path)

        return save_path




