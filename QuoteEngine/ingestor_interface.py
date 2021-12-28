"""Quote Engine Module, file for Ingestor interface."""
from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface for all parsers."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        """Determine if parser works on given path."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse content via path to files to quotes."""
        pass
