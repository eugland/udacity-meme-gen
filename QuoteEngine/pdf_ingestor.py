"""Quote Engine Module, File containing PDF ingestor."""
import os
import random
import subprocess

from typing import List
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """PDF Ingestor that parse pdf into quotes."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse str to quotes path, and return a quotes list."""
        if not cls.can_ingest(path):
            raise IOError('Cannot Ingest Exception')

        quotes = []

        os.makedirs("./tmp", exist_ok=True)
        tmp = f"./tmp/{random.randint(0, 10000000)}.txt"

        try:
            call = subprocess.call(["pdftotext", path, tmp])
        except FileNotFoundError:
            print(path, "not found!")

        with open(tmp, "r") as f:
            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(body, author))

        if os.path.exists(tmp):
            os.remove(tmp)

        return quotes
