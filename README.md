# **FinalTask\_Jubelio**

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## 📌 **Deskripsi Project**

**FinalTask\_Jubelio** adalah project **automation testing** berbasis **Python + Selenium** yang dikembangkan sebagai bagian dari **Final Project Internship Rakamin Academy x Jubelio**.
Project ini bertujuan untuk menguji fitur-fitur utama pada website Jubelio, termasuk:

* Proses **login user**
* **Manajemen stok** produk pada sistem

Automation testing ini dibuat untuk mempermudah proses pengujian, menghemat waktu, dan memastikan kualitas aplikasi tetap terjaga.

---

## 🧩 **Fitur Utama**

* ✅ **Login Automation** → Mengotomatisasi proses login pada website Jubelio.
* ✅ **Stock Management Automation** → Menguji penambahan, pembaruan, dan penghapusan stok produk.
* ✅ **Cross-Browser Testing** → Mendukung eksekusi di berbagai browser seperti Chrome, Firefox, dan Edge.
* ✅ **WebDriver Management** → Menggunakan **webdriver-manager** untuk instalasi dan update driver otomatis.
* ✅ **Scalable & Maintainable** → Kode ditulis dengan struktur yang mudah dipelihara.

---

## 🏗️ **Struktur Project**

```bash
FinalTask_Jubelio/
├── Login automation.py     # Script otomatisasi untuk login Jubelio
├── Manage Stock.py         # Script otomatisasi untuk manajemen stok
├── requirements.txt        # Daftar dependencies Python (opsional)
├── README.md               # Dokumentasi project
└── __pycache__/            # Cache Python (otomatis terbentuk)
```

---

## 🛠️ **Teknologi yang Digunakan**

| **Teknologi**           | **Fungsi**                                   |
| ----------------------- | -------------------------------------------- |
| **Python 3.10+**        | Bahasa pemrograman utama                     |
| **Selenium WebDriver**  | Framework untuk otomatisasi testing          |
| **Webdriver-Manager**   | Mengatur driver browser otomatis             |
| **Visual Studio Code**  | Code editor utama                            |
| **Pytest** *(opsional)* | Untuk menjalankan testing secara terstruktur |

---

## ⚡ **Instalasi & Setup**

### **1. Clone Repository**

```bash
git clone https://github.com/agilwidianto/FinalTask_Jubelio.git
cd FinalTask_Jubelio
```

### **2. Setup Virtual Environment** *(opsional tapi direkomendasikan)*

```bash
python -m venv venv
source venv/bin/activate      # Untuk MacOS/Linux
venv\Scripts\activate         # Untuk Windows
```

### **3. Install Dependencies**

```bash
pip install selenium
pip install webdriver-manager
```

Atau jika kamu menambahkan file **requirements.txt**:

```bash
pip install -r requirements.txt
```

---

## ▶️ **Cara Menjalankan Project**

### **1. Menjalankan Login Automation**

```bash
python "Login automation.py"
```

### **2. Menjalankan Stock Management Automation**

```bash
python "Manage Stock.py"
```
