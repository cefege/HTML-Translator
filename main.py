from translation_module import simple_html_translate, html_translate

translated_html = simple_html_translate("<b>Hello</b>", source_language='en', target_language='es')
translated_html_simple = html_translate("<YOUR HTML HERE>", source_language='en', target_language='es')

print(translated_html)
print(translated_html_simple)

