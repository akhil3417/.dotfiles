#!/bin/bash
#generate toc for pdf documents
# https://pypi.org/project/pdf.tocgen/
# https://krasjet.com/voice/pdf.tocgen/#one-more-example-mathematics
# pip install -U pdf.tocgen
rm recipe.toml
rm toc
# Check if all required arguments are provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 pdf_filename page1 heading1 page2 heading2 page3 heading3 page4 heading4"
  exit 1
fi

# Extract metadata for headings
pdfxmeta -a 1 -p $2 "$1" "$3" >> recipe.toml
pdfxmeta -a 2 -p $4 "$1" "$5" >> recipe.toml
pdfxmeta -a 3 -p $6 "$1" "$7" >> recipe.toml
pdfxmeta -a 4 -p $8 "$1" "$9" >> recipe.toml

# Generate and import table of contents
pdftocgen "$1" < recipe.toml | pdftocio -o toc.pdf "$1"

# Or edit the table of contents before importing it
pdftocgen "$1" < recipe.toml > toc
pdftocio "$1" < toc
