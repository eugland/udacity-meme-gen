"""Quote Engine Module file containing the Quote Model."""


class QuoteModel:
    """QuoteModel stores the quote and its author."""

    def __init__(self, body, author):
        """Initialize for the Quote Model."""
        self.body = body
        self.author = author

    def __str__(self):
        """Output the Quote."""
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Output a representation of the Quote Model."""
        return f'QuoteModel(body={self.body}, author={self.author})'
