# 🔐 SecureVault – Zero-Knowledge Password Manager

SecureVault is a **zero-knowledge password manager** built from scratch.  
The goal: showcase security-first design with **end-to-end encryption**, a strong **key derivation function (Argon2id)**, and local-only storage.  

This project starts simple (CLI or Desktop app) and grows into a full-featured password manager with sync, biometrics, and even a browser extension.

---

## 🚀 Project Goals
- Build a **secure, zero-knowledge vault** for storing credentials.  
- Learn and demonstrate **modern cryptography practices**.  
- Showcase a **real-world portfolio project** for security & development.  

---

## 🛡️ Threat Model

### Protects against:
- Stolen database or local vault files.  
- Device theft (if master password is strong).  
- Brute-force attempts (Argon2id with sane defaults).  

### Not (yet) protected against:
- Malware or keyloggers on the client device.  
- Social engineering (phishing, shoulder surfing).  
- Advanced side-channel attacks (timing, memory scraping).  

---

## 📦 MVP Features
- Master password → derives encryption key.  
- Local-only vault (encrypted SQLite/JSON).  
- Add, view, edit, delete entries.  
- Clipboard copy with auto-clear.  
- Auto-lock/timeout when inactive.  

---

## 🌱 Future Roadmap
- ✅ Password generator.  
- ✅ Tagging & search.  
- 🔜 Biometric unlock (FaceID/Fingerprint).  
- 🔜 Server sync with **zero-knowledge** architecture.  
- 🔜 Browser extension for autofill.  
- 🔜 Breach check integration (HaveIBeenPwned API).  

---

## 🖼️ Wireframes (text version)
**Login Screen**  
- Input: Master password  
- Button: Unlock Vault  

**Vault Screen**  
- List entries (title + username)  
- Buttons: Add / Edit / Delete  
- Lock / Logout  

**Add/Edit Screen**  
- Fields: Title, Username, Password, Notes  
- Button: Save  

---

## 🛠️ Tech Stack (Planned)
- **Phase 1:** Python (CLI) + `cryptography` + `argon2-cffi` + SQLite  
- **Phase 2+:** React + Electron for Desktop UI  
- **Phase 3+:** FastAPI (backend for sync) + PostgreSQL  
- **Phase 4+:** React Native for Mobile + Biometrics  

---

## 📚 Learning Outcomes
- Hands-on with **AES-GCM / XChaCha20-Poly1305** authenticated encryption.  
- Implementing **Argon2id KDF** for password hardening.  
- Designing **zero-knowledge systems** (server stores only encrypted blobs).  
- Understanding real-world security tradeoffs.  

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to fork, star ⭐, and submit pull requests.  

---


---
