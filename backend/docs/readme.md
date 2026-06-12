# Skenario pendaftaran user

```text
Register
      │
      ▼
Simpan user
is_active = False
email_verified_at = NULL
verify_email_token = NULL
      │
      ▼
User Login
      │
      ├── email sudah verified
      │          │
      │          ▼
      │      masuk aplikasi
      │
      └── email belum verified
                 │
                 ▼
Frontend tampilkan tombol
"Verifikasi Email"
                 │
                 ▼
POST /user/send-verification-email
                 │
                 ▼
Backend generate token
simpan ke database
                 │
                 ▼
Kirim email
```