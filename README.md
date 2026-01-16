# 🔎 JS Endpoint Extractor

JS Endpoint Extractor is a Python-based CLI tool that scans a webpage,
collects linked JavaScript files, and extracts possible API endpoints
directly from the JavaScript source code.

It is designed for reconnaissance and learning how client-side code
often reveals backend endpoints.

---

## Overview

Modern web applications rely heavily on JavaScript.
APIs, routes, and internal endpoints are often referenced directly
inside JS files.

This tool:
- Fetches a target webpage
- Extracts linked `.js` files
- Downloads each JavaScript file
- Searches for common API-style endpoint patterns

The result is a quick overview of potential endpoints worth further testing.

---

## Features

- Extracts JavaScript file URLs from a webpage
- Handles relative and absolute script paths
- Scans JavaScript source code for API endpoints
- Supports optional output saving to a file
- Simple and beginner-friendly workflow

---

## How It Works

The script requests the target webpage and parses its HTML
to find all `<script src="...">` references.

Each JavaScript file is then fetched,
and regex patterns are applied to locate endpoint-like paths
such as `/api/`, `/v1/`, or `/v2/`.

All unique endpoints are collected and displayed or saved.

---

## Usage

Run the tool exactly like this  
python js_extract.py -u <url>

To save results to a file  
python js_extract.py -u <url> -o output.txt

---

## Output

If no output file is specified:
- All discovered endpoints are printed to the terminal

If an output file is provided:
- Endpoints are written to the specified file
- A confirmation message is shown

---

## Requirements

- Python 3.x
- requests library

Install dependencies if needed  
pip install requests

---

## Notes

- Endpoint detection is pattern-based
- Some endpoints may be false positives
- Intended for learning and authorized reconnaissance only

---

## Final Thoughts

Backend logic often leaks through frontend code.
If you can read JavaScript,
you can discover a lot without sending a single payload.
