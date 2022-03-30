from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def html_translate(html_text: str, source_language: str = 'en', target_language: str = 'es',
                   debug: bool = False) -> str:
    """
    Function That Takes Input HTML and The Source and Target Language, Then Return The Translated HTML
    :param html_text: The raw HTML
    :param source_language: The translation source language
    :param target_language: The translation target language
    :param debug: set to true to know more about issues and corner cases
    :return: The Translated HTML
    """
    # Initiate The Translator (I Prefer Google Translator But You Can Choose Any Other Translator From This List)
    # (GoogleTranslator, MicrosoftTranslator, PonsTranslator, LingueeTranslator, MyMemoryTranslator, YandexTranslator,
    # PapagoTranslator, DeeplTranslator, QcriTranslator, single_detection, batch_detection)
    translator = GoogleTranslator(source=source_language, target=target_language)

    translation_mapping_dict = {}
    translation_list = []
    # Parse The HTML File Using BeautifulSoup Library
    html_parser = BeautifulSoup(html_text, features="html.parser")

    # Loop On All Strings and Keep String Into translation_list
    for st in html_parser.strings:
        # Keep The Next Element Before Changing The Current One
        next = st.next_element
        # Keep the Text in The Translation List
        translation_list.append(str(st))
        # Assign The Next Element in The HTML Tree
        st.next_element = next

    placeholder = "\n====[({0-0})]====\n"
    # Now, We Have One List Contains All Strings. We will Convert it into paragraph

    paragraph = placeholder.join(translation_list)

    # Then, We Will translate the paragraph at once
    translation = translator.translate(paragraph)

    # Translate Placeholder
    placeholder_translated = translator.translate(placeholder)

    # Finally, We will Convert The Translated Paragraph again into List
    trans_paragraph_list = translation.split(placeholder_translated)

    if debug and (len(trans_paragraph_list) != len(translation_list)):
        print(f"Original Content:\n{html_parser}\n=============\nTranslated Content:\n{trans_paragraph_list}")

    # Loop On The HTML Again
    for idx, st in enumerate(html_parser.strings):
        # Keep The Next Element Before Changing The Current One
        next = st.next_element
        # Check if Translation input is valid. Numbers and Punctuations are kept as it is.
        try:
            # Replace Original String With The Translated One
            st.replace_with(trans_paragraph_list[idx])
        except Exception as e:
            print(f"Error Occurred: {e}")
        # Assign The Next Element in The HTML Tree
        st.next_element = next
    return str(html_parser)


def simple_html_translate(html_text: str, source_language: str = 'en', target_language: str = 'es') -> str:
    """
    Function That Takes Input HTML and The Source and Target Language, Then Return The Translated HTML
    :param html_text: The raw HTML
    :param source_language: The translation source language
    :param target_language: The translation target language
    :return: The Translated HTML
    """
    # Initiate The Translator (I Prefer Google Translator But You Can Choose Any Other Translator From This List)
    # (GoogleTranslator, MicrosoftTranslator, PonsTranslator, LingueeTranslator, MyMemoryTranslator, YandexTranslator,
    # PapagoTranslator, DeeplTranslator, QcriTranslator, single_detection, batch_detection)
    translator = GoogleTranslator(source=source_language, target=target_language)

    translation_mapping_dict = {}
    translation_list = []
    # Parse The HTML File Using BeautifulSoup Library
    html_parser = BeautifulSoup(html_text, features="html.parser")

    # Loop On All Strings
    for st in html_parser.strings:
        # Keep The Next Element Before Changing The Current One
        next = st.next_element

        # Check if Translation input is valid. Numbers and Punctuations are kept as it is.
        try:
            # Translate The String
            translation = translator.translate(st)
            # Replace The Original String By The Translation
            st.replace_with(translation)
        except Exception as e:
            print(f"Exception Occurred: {e}")
        # Assign The Next Element in The HTML Tree
        st.next_element = next

    return str(html_parser)
