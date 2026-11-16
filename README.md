# Markdown Conversion Utilities

A lightweight, dual-environment utility suite designed to eliminate documentation friction by instantly converting raw text chunks and CSV data into clean, formatted Markdown tables.

Built with both backend processing (Python) and interactive frontend execution (HTML/JavaScript) in mind.

---

## 📂 Repository Structure

```text
markdown-conversion-utilities/
├── README.md                  # Project documentation
├── python/
│   ├── csv_to_markdown.py     # Python backend CSV-to-Markdown converter
│   └── text_to_markdown.py    # Python text chunk (Time/Focus/Activity) parser
└── web/
    ├── csv_converter.html     # Interactive browser-based CSV converter with dark mode
    └── text_converter.html    # Interactive browser-based text chunk converter with dark mode
```

##🚀 Key Features
* **Dual-Language Implementation:** Fully realized conversion logic in both Python (for data pipelines and scripting) and JavaScript (for instant browser execution).

* **CSV Parsing:** Takes standard CSV data and auto-generates Markdown tables with proper header separators.

* **Structured Text Chunking:** Specialized parser designed to convert multiline chronological notes (Time Block, Focus Area, Core Activity) into clean documentation tables.

* **Interactive Web Tools:** Standalone HTML files featuring a clean blog-like layout, responsive design, and built-in Dark Mode support.

* **Zero Heavy Dependencies:** The web tools run entirely client-side in any modern browser without requiring servers or external node packages.

##🛠️ Usage Instructions


###1. Python Utilities
Run the Python scripts directly from your terminal to process data programmatically or within data pipelines:

```Bash
# Convert CSV text
python3 python/csv_to_markdown.py

# Convert structured text chunks
python3 python/text_to_markdown.py
```


###2. Web Utilities
Open either HTML file directly in any browser (such as Google Chrome) to use the interactive interface:

* Double-click web/csv_converter.html or web/text_converter.html, paste your raw data, and instantly copy your generated Markdown table.

##💡 Author
Developed as part of an ongoing independent technical documentation and system workflow automation project.
