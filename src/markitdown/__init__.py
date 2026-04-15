"""MarkItDown - Convert various file formats to Markdown.

This package provides utilities to convert documents, spreadsheets,
presentations, images, and other file types into Markdown format.
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

__version__ = "0.1.0"
__all__ = ["MarkItDown", "DocumentConverter", "ConversionResult"]
