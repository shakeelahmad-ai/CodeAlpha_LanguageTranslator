from gtts import gTTS
import pyperclip
import os
import streamlit as st
from config import APP_NAME, PAGE_ICON, LANGUAGES, HISTORY_FILE
from translator import Translator
from utils import add_history

st.set_page_config(
    page_title=APP_NAME,
    page_icon=PAGE_ICON,
    layout="centered"
)

st.title("🌍 Language Translator Tool")
st.subheader("CodeAlpha Internship Project")
st.write("Developed by **Shakeel Ahmad**")

source = st.selectbox(
    "Select Source Language",
    list(LANGUAGES.keys())
)

target = st.selectbox(
    "Select Target Language",
    list(LANGUAGES.keys())
)

text = st.text_area(
    "Enter Text",
    height=180
)


if st.button("Translate"):
    if text.strip():

        translated = Translator.translate(
            text,
            LANGUAGES[source],
            LANGUAGES[target]
        )

        st.success("Translation Completed Successfully")

        st.text_area(
            "Translated Text",
            translated,
            height=180
        )

        add_history(HISTORY_FILE, text, translated)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📋 Copy Translation"):
                pyperclip.copy(translated)
                st.success("Copied Successfully!")

        with col2:
            tts = gTTS(
                text=translated,
                lang=LANGUAGES[target]
            )

            tts.save("voice.mp3")

            with open("voice.mp3", "rb") as audio:
                st.audio(audio.read())

    else:
        st.warning("Please enter some text.")

st.divider()

st.caption("© 2026 Shakeel Ahmad | CodeAlpha Internship Project")