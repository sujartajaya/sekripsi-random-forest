# Algoritma user

## Register user

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

## Login user
```text
Login
      │
      ▼
cek username
      │
      ▼
cek password
      │
      ▼
create_access_token(
    {
        "user_id": user.id
    }
)
      │
      ▼
JWT
      │
      ▼
Frontend simpan JWT
      │
      ▼
Authorization: Bearer xxxxxx
      │
      ▼
get_current_user()
      │
      ▼
decode_token()
      │
      ▼
ambil user_id
      │
      ▼
SELECT * FROM users
WHERE id=user_id
      │
      ▼
return User
```