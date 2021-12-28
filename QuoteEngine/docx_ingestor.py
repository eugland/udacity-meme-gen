"""Quote Engine Package, file for Docx Ingestor."""
from typing import List

from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface
import docx


class DocxIngestor(IngestorInterface):
    """Docx Ingestor that parse Docx to string list."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse only docx type."""
        if not cls.can_ingest(path):
            raise IOError('Cannot Ingest Exception')

        quotes = []
        df = docx.Document(path)
        for para in df.paragraphs:
            if para.text != '':
                body, author = para.text.split(" - ")
                quotes.append(QuoteModel(body, author))

        return quotes
