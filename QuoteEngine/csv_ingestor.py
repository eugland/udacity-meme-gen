"""Quote Engine Package, file for CSV ingestor."""
from typing import List

from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface
import pandas


class CSVIngestor(IngestorInterface):
    """CSVIngestor that parses only csv."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse data via csv path to a list of quote models."""
        if not cls.can_ingest(path):
            raise IOError('Cannot Ingest Exception')

        df = pandas.read_csv(path, header=0)
        return [QuoteModel(f'"{body}"', author) for body, author in zip(df['body'], df['author'])]