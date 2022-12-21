# wiktionary-markdown
download wiktionary entries as markdown notes

## usage
- `wiktdl.py`: download entry html (for templates are not rendered raw wikitext)
- `wiktmd.sh`: convert that html into markdown with pandoc and adjust the format (internal wiki links converted into `[[...]]`)
- `export_pdf.sh`: convert markdown to pdf (using pandoc) with internal links removed
