import streamlit as st
import requests
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Hugging Face API anahtarı
hf_api_key = os.getenv("HF_API_KEY")

# Sayfa başlığı
st.set_page_config(page_title="AI Cover Letter Generator", page_icon="💌")
st.title("💌 AI Cover Letter Generator")
st.write("Yapay zeka destekli profesyonel ön yazı oluşturma aracı.")

# Kullanıcı bilgilerini al
name = st.text_input("Ad Soyad", "Güler Göçmen")
position = st.text_input("Pozisyon", "AI & Python Developer")
company = st.text_input("Şirket Adı", "OpenAI")
skills = st.text_area("Teknik Beceriler", "Python, Machine Learning, Data Science, AI Projects")
motivation = st.text_area("Motivasyon", "I am passionate about artificial intelligence and eager to contribute innovative solutions.")

# Buton
if st.button("✨ Cover Letter Oluştur"):
    if not hf_api_key:
        st.error("⚠️ API anahtarı bulunamadı! Lütfen .env dosyasına HF_API_KEY ekleyin.")
    else:
        with st.spinner("Yapay zeka cover letter oluşturuyor..."):
            # İstek metni (prompt)
            prompt = (
                f"Write a professional and concise cover letter for {name}, "
                f"applying for the position of {position} at {company}. "
                f"Highlight skills: {skills}. "
                f"Motivation: {motivation}. "
                f"Keep it polite, structured, and inspiring."
            )

            # Hugging Face API isteği
            response = requests.post(
                "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
                headers={"Authorization": f"Bearer {hf_api_key}"},
                json={"inputs": prompt},
            )

            # Yanıt kontrolü
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and "summary_text" in result[0]:
                    cover_letter = result[0]["summary_text"]
                else:
                    cover_letter = result

                st.success("✅ Cover Letter başarıyla oluşturuldu!")
                st.write(cover_letter)
            else:
                st.error(f"❌ Model hatası: {response.status_code}")
                st.write(response.text)
