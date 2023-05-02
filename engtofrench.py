# -*- coding: utf-8 -*-
"""EngtoFrench.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cDTz-nKqrKd2vR-mOrjszzAhRcwXB1pu
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install transformers pandas

import pandas as pd

# Change the path to the location of the extracted text file on your Google Drive
df = pd.read_csv('/content/drive/MyDrive/EtF/fra.txt', sep='\t', header=None, names=['English', 'French'])

from transformers import pipeline

# Load the pre-trained translation model
translator = pipeline('translation_en_to_fr')

def translate_word(word):
    # Use the pre-trained model to translate the word
    translation = translator(word, max_length=40)

    # Return the translated word
    return translation[0]['translation_text']

# Prompt the user to enter an English word
word = input('Enter an English word to translate: ')

# Translate the word using the pre-trained model
translation = translate_word(word)

# Print the translated word
print(f'Translation: {translation}')