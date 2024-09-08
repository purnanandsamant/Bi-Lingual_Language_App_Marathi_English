#!/usr/bin/env python
# coding: utf-8

# # Bilingual Conversation app - Marathi_English Conversation

# <span style="font-size: 30px; color: blue; font-style: italic; font-weight: bold;">Import Libraries</span>

# In[ ]:


import streamlit as st
from streamlit_mic_recorder import speech_to_text
from deep_translator import GoogleTranslator
from gtts import gTTS
import io


# <span style="font-size: 30px; color: blue; font-style: italic; font-weight: bold;">Define Functions</span>

# In[ ]:


def translate_text(text, source_lang, target_lang):
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)
    except Exception as e:
        return f"Translation error: {str(e)}"

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.getvalue()


# <span style="font-size: 30px; color: blue; font-style: italic; font-weight: bold;">Design Streamlit App</span>

# In[ ]:


st.markdown("<h1 style='font-size: 24px;'>Marathi-English Voice Translator</h1>", unsafe_allow_html=True)

st.markdown("## Marathi to English")
marathi_speech = speech_to_text(language='mr', key='marathi_speech')
if marathi_speech:
    st.write(f"Marathi: {marathi_speech}")
    english_translation = translate_text(marathi_speech, 'mr', 'en')
    st.write(f"English: {english_translation}")
    
    english_audio = text_to_speech(english_translation, 'en')
    st.audio(english_audio, format="audio/mp3")

st.markdown("---")

st.markdown("## English to Marathi")
english_speech = speech_to_text(language='en', key='english_speech')
if english_speech:
    st.write(f"English: {english_speech}")
    marathi_translation = translate_text(english_speech, 'en', 'mr')
    st.write(f"Marathi: {marathi_translation}")
    
    marathi_audio = text_to_speech(marathi_translation, 'mr')
    st.audio(marathi_audio, format="audio/mp3")

