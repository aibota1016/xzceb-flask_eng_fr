"""
This module leverages the IBM Watson language translator API 
to translate from English to French and vice versa
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = 'kBiGdM1OBs7Zv3SWmazGyBYyCTUP47NsXfp6bFv1CYo2'
URL = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/3a8e38d3-a336-4f1c-8ac7-ef6ce17a9321'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)
languages = language_translator.list_languages().get_result()

def english_to_french(english_text):
    """translates from English to french"""
    response = language_translator.translate(
        text=english_text, model_id='en-fr')
    french_text = response.get_result()
    return french_text

def french_to_english(french_text):
    """translates from French to English"""
    response = language_translator.translate(
        text=french_text, model_id='fr-en')
    english_text = response.get_result()
    return english_text
