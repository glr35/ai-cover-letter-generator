# 💌 AI Cover Letter Generator

Bu proje, **Hugging Face API** kullanarak otomatik olarak profesyonel bir **ön yazı (cover letter)** oluşturan yapay zeka tabanlı bir web uygulamasıdır.  
Kullanıcıdan aldığı bilgilerle kişiye özel, özgün ve akıcı bir şekilde profesyonel ön yazı üretir.

---

## 🚀 Özellikler

- 🧠 Yapay Zeka destekli cover letter üretimi  
- 👩‍💼 Kullanıcıdan ad, pozisyon, şirket, beceriler gibi bilgileri alır  
- ⚡ Hugging Face Inference API ile hızlı cevap üretimi  
- 🎨 Streamlit tabanlı modern kullanıcı arayüzü  
- 🔐 `.env` dosyası ile güvenli API anahtarı yönetimi  
- 💾 Sonuçları kolayca kopyalama veya indirme imkânı  

---

## 🧠 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|------------|----------|
| 🐍 Python 3.12 | Ana programlama dili |
| 🎨 Streamlit | Web arayüzü oluşturma |
| 🤗 Hugging Face | AI model barındırma ve metin üretimi |
| 🔐 python-dotenv | Ortam değişkeni yönetimi |
| 🌐 Requests | API istekleri gönderme |

---

## ⚙️ Kurulum

Projeyi kendi bilgisayarında çalıştırmak için şu adımları izle:

```bash
# 1️⃣ Projeyi klonla
git clone https://github.com/glr35/ai-cover-letter-generator.git

# 2️⃣ Proje klasörüne gir
cd ai-cover-letter-generator

# 3️⃣ Sanal ortam oluştur ve etkinleştir
python -m venv .venv
.venv\Scripts\activate

# 4️⃣ Gerekli bağımlılıkları yükle
pip install -r requirements.txt

# 5️⃣ .env dosyası oluştur
# İçerisine şu satırı ekle (kendi token’inle değiştir)
HF_API_KEY=hf_xxx_senin_tokenin

# 6️⃣ Uygulamayı çalıştır
streamlit run app.py
🧾 Örnek Kullanım
Uygulamayı çalıştırdıktan sonra:

Adını, başvurduğun pozisyonu, şirket adını ve becerilerini gir.

“✨ Cover Letter Oluştur” butonuna tıkla.

Yapay zeka senin için profesyonel bir ön yazı üretecek.

📸 Örnek Ekran:
(Eğer istersen buraya uygulamadan bir ekran görüntüsü ekleyebiliriz.)

📂 Proje Dosya Yapısı
bash
Kodu kopyala
ai-cover-letter-generator/
│
├── app.py              # Ana uygulama dosyası
├── .env                # Hugging Face API anahtarı
├── requirements.txt    # Gerekli Python kütüphaneleri
└── README.md           # Proje açıklaması
👩‍💻 Geliştirici
👩‍💻 Güler Göçmen
AI & Python Developer

🌐 LinkedIn
💻 GitHub
📧 gulergocmen@example.com

🏷️ Etiketler
#Python #Streamlit #HuggingFace #AI #CoverLetter #Portfolio #GülerGöçmen

© 2025 Güler Göçmen — Tüm hakları saklıdır.

markdown
Kodu kopyala

---

### 🔧 Nasıl ekleyeceksin:
1. VS Code’da projenin içine git → `C:\Users\Güler Göçmen\Desktop\ai-cover-letter-generator`
2. Yeni dosya oluştur → `README.md`
3. Yukarıdaki içeriği **tamamını kopyala → yapıştır**
4. Kaydet (`Ctrl + S`)
5. Terminalde sırayla:
   ```bash
   git add README.md
   git commit -m "Add professional README file"
   git push -u origin main
