# HTML Translator

## Installation
### Using pip
```angular2html
pip install git+https://github.com/cefege/HTML-Translator.git 
```
or clone the repository
```angular2html
git clone https://github.com/cefege/HTML-Translator.git
```
## Usage
1. Import `translation_module.py` 
```
from translation_module import simple_html_translate, html_translate
```
2. Use one of these two functions `simple_html_translate` or `html_translate` as follows
```
translated_html = simple_html_translate("<YOU HTML HERE>", source_language='en', target_language='es')
# OR
translated_html_simple = html_translate("<YOUR HTML HERE>", source_language='en', target_language='es')
```
3. Export the translated HTML to any format

## Notes
1. `simple_html_translate` sends multiple API Requests (One request per every string) which is simple but more costly.
2. `html_translate` send one API Request for the whole file which is somehow complex but less costly.