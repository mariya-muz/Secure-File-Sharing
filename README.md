# Secure File Sharing System – Internee.pk

Secure file-sharing project using **Flask, AES-256 encryption, AWS S3 storage, IAM roles, and signed URLs** to demonstrate secure, controlled, and resilient file exchange practices between internal teams and external parties.

---

## Internship Deliverables

### 1. Local Upload

Developed Flask-based portal for file upload.

- Verified successful upload via local server (`127.0.0.1:5000/upload`).
- File stored in local `uploads` directory.

<img width="1000" height="800" alt="4 upload-success" src="https://github.com/user-attachments/assets/8bb14f53-9afe-4143-96a1-07e460b5dc88" />


*Context: Shows confirmation message and file saved locally.*

---

### 2. File Encryption

Implemented AES-256 encryption for uploaded files.

- Converted plaintext files into `.encrypted` format.
- Verified ciphertext stored securely.

<img width="1773" height="917" alt="5 encrypted-success" src="https://github.com/user-attachments/assets/84496280-336f-418c-875e-0f45dd1b09dc" />



*Context: Displays encrypted file contents in text editor.*

---

### 3. AWS S3 Bucket Setup

Created dedicated S3 bucket `mariya-secure-file-sharing`.

- Configured bucket for encrypted file storage.
- Verified initial empty state before uploads.

<img width="1000" height="600" alt="6 s3-bucket" src="https://github.com/user-attachments/assets/2a36ba78-6cc1-445a-bca3-fc787295e2d8" />


*Context: Shows bucket with no objects.*

---

### 4. IAM User Configuration

Created IAM user `secure-file-user`.

- Attached **AmazonS3FullAccess** policy.
- Generated access keys for programmatic access.

<img width="1000" height="800" alt="7 iam-user" src="https://github.com/user-attachments/assets/8c7b568c-c2ff-4754-9d62-33512714627e" />


*Context: Displays IAM user details with attached policy.*

---

### 5. Encrypted File Upload to S3

Uploaded encrypted files to S3 bucket.

- Verified object metadata (size, type, timestamp).
- Storage class: Standard.

<img width="1250" height="900" alt="8 bucket-upload" src="https://github.com/user-attachments/assets/1c2d8f17-3ff2-442f-aa8f-ccd6d77efea8" />


*Context: Shows `.encrypted` file stored in bucket.*

---

### 6. Signed URL Generation

Implemented signed URLs for controlled access.

- Generated temporary download links.
- Verified expiration-based access control.

<img width="1122" height="552" alt="9 download-encrypted" src="https://github.com/user-attachments/assets/c6bc604a-e7b8-4348-a025-dbb56ad4650c" />

*Context: Portal provides link to download encrypted file.*

---

### 7. File Decryption

Decrypted files after download.

- Verified restored original format.
- Stored decrypted files in local directory.

<img width="1159" height="899" alt="10 decrypt-success" src="https://github.com/user-attachments/assets/80baf164-390d-48b0-a961-a35b21297bbf" />


*Context: Shows decrypted file saved locally.*

---

### 8. Frontend Interface

Developed simple upload interface.

- HTML/CSS frontend with Flask backend.
- Buttons: Choose File, Upload.

<img width="1633" height="988" alt="11 css" src="https://github.com/user-attachments/assets/a889822b-006d-4dd6-9a75-e232290cec7e" />


*Context: Displays Secure File Sharing System homepage.*

---

### 9. Dataset Integration

Tested system with Kaggle datasets.

- Imported Netflix dataset (`titles.csv`).
- Encrypted, uploaded, and decrypted dataset.

<img width="1254" height="1033" alt="12 kaggle" src="https://github.com/user-attachments/assets/05888c63-b0c3-4439-a369-a2027a63c2f7" />


*Context: Shows dataset imported and encrypted.*

---

### 10. Local + Cloud Sync

Maintained encrypted files both locally and in S3.

- Verified consistency across environments.

<img width="1751" height="931" alt="13 dataset-success" src="https://github.com/user-attachments/assets/3125a815-6886-4466-b3e1-5e25dd7cab33" />


*Context: Displays encrypted files in local folder and S3 bucket.*

---

### 11. Dataset Analysis

Opened decrypted dataset in Excel.

- Verified columns: title, type, release year, genres, IMDb/TMDB scores.

<img width="1810" height="1129" alt="14 dataset-decrypt" src="https://github.com/user-attachments/assets/0d6e51ee-d9e3-43dc-b692-ae500d42ca7b" />


*Context: Shows decrypted CSV opened in Excel.*

---

### 12. Codebase

Developed Flask app (`app.py`) and HTML template (`index.html`).

- Flask routes for upload, encryption, decryption.
- HTML frontend for user interaction.

<img width="1807" height="610" alt="1 vscode" src="https://github.com/user-attachments/assets/4f96878f-4430-4954-a670-e4ac01f602cd" />


*Context: Displays source code in VS Code.*

---

### 13. Environment Setup

Installed dependencies (`flask`, `boto3`, `cryptography`).

- Generated `requirements.txt`.
- Verified Flask server running locally.

<img width="1919" height="1156" alt="2 cmd" src="https://github.com/user-attachments/assets/c76cdf18-da25-4324-bbf1-b8919425bab3" />


*Context: Shows pip installs and server run output.*

---

## Summary of Security Measures Implemented

- End-to-end encryption for file uploads/downloads.
- Secure storage in AWS S3 bucket.
- IAM user with restricted permissions.
- Signed URLs for controlled access.
- Local + cloud redundancy for encrypted files.
- Dataset integration for testing and validation.

---

## Results & Learnings

- **Encryption & Security**
    - Successfully implemented **AES-256 encryption** for end-to-end file protection.
    - Learned how to manage encryption keys securely and apply cryptography libraries in Python.
- **Cloud Integration**
    - Configured **AWS S3 bucket** for encrypted file storage.
    - Gained hands-on experience with **IAM roles and policies** for least-privilege access.
    - Practiced secure file operations using **Boto3 SDK**.
- **Access Control**
    - Implemented **signed URLs** to enforce temporary, controlled access.
    - Understood how signed URLs prevent unauthorized downloads and ensure compliance.
- **System Workflow**
    - Built a complete pipeline: **upload → encrypt → store → signed URL → download → decrypt**.
    - Validated workflow with both sample reports and Kaggle datasets.
- **Practical Skills Gained**
    - Flask web development (routes, templates, server setup).
    - Python environment management (`venv`, `requirements.txt`).
    - AWS cloud security fundamentals (IAM, S3, access keys).
    - Data handling and validation with real-world datasets.
