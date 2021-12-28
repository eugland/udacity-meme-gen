"""File containing the TxtIngestor."""
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Ingests a .txt file."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the content of a path to return a list of QuoteModel objects.

        Args:
            path (str): Path to file.
        Returns:
            List[QuoteModel]: List[QuoteModel]: List of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []

        with open(path, "r", encoding="utf-8-sig") as f:
            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(f"'{body}'", author))
        return quotes
