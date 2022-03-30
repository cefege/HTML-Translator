import os
from os import path

import pandas as pd
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from tqdm import tqdm

# Input CSV File (Change This Path To The CSV File Path On Your Machine)
CSV_FILE_PATH = "/home/nassar/Desktop/testagain/1000samples_html_translate_test (1).csv"

# Data Output Directory (Change This Path To Any Empty Directory To Export HTML Files To it)
OUTPUT_DIR = "/home/nassar/Desktop/testagain/oo"

# Output CSV File (Don't Change This Line it Will be Beside The Original File)
OUTPUT_CSV = f"{path.join(path.dirname(CSV_FILE_PATH), f'trans_{path.basename(CSV_FILE_PATH)}')}"

# Confirm That Output Directory Existed, Else, Create One
if not path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

# Read CSV File
df = pd.read_csv(CSV_FILE_PATH, header=0)

# Calculate Number of Digits (Used to Format Output File Name)
n_digits = len(str(len(df['Text'])))

# Append Output Data to Assign Them to The DataFrame
output_column = []


def html_translate(html_text: str, source_language: str = 'en', target_language: str = 'es') -> str:
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
    return html_parser


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


if __name__ == '__main__':
    # Loop On Each Row
    for file_idx, html_file in enumerate(tqdm(df['Text'].to_list())):
        # Format Output Path
        output_path = path.join(OUTPUT_DIR, f"File_{file_idx:0{n_digits}d}")

        # Translate The whole Page
        translated_html = html_translate(html_file, "en", "es")
	# OR
	#translated_html = simple_html_translate(html_file, "en", "es")
	
        # Append Output Column To The List
        output_column.append(str(translated_html))

        # Write The Original HTML File
        with open(f"{output_path}_orig.html", "w") as fout_orig:
            fout_orig.write(html_file)

        # Write The translated HTML File
        with open(f"{output_path}_trans.html", "w") as fout_trans:
            fout_trans.write(str(translated_html))

    # Assign The Result Column
    df['translated_html'] = output_column

    # Export The Final CSV File
    df.to_csv(OUTPUT_CSV)

    print(f"Files Converted Successfully")
