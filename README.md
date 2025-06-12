# SupaUser 🏋️‍♂️

**SupaUser** is a lightweight microservice built with **Python 3.12** and **FastAPI**, designed to centralize and streamline user authentication and JWT management via **Supabase**. It offers a scalable, secure, and consistent approach to handling user authentication across multiple projects, adapting to diverse requirements with its modular architecture.

## Features ✨
- **Centralized Authentication:** A single service for managing user login, JWT generation, and validation.
- **Secure Token Management:** Robust handling of JWTs to ensure efficient access control.
- **Supabase Integration:** Seamless connection with Supabase for user data and authentication.
- **Modular & Scalable:** Easily adaptable to projects with varying user data needs.

## Overview 🔍
SupaUser simplifies the authentication process by isolating user management into a dedicated microservice. This not only enhances security but also streamlines maintenance and accelerates development across different applications. Whether you require a single contact detail or support for multiple configurations, Supa-User's flexible design has you covered.

## Getting Started 🛠️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/feniuspw/supa-user
   cd supa-user


2. **Create your .env based on .env.example:**
   - Defina `SUPABASE_URL` e `SUPABASE_API_KEY`.
   - Opcionalmente defina `SSO_REDIRECT_TO` para o callback do SSO com Google, Microsoft ou GitHub.

3. **Run SupaUser with docker:**
   ```bash
   docker compose up -d
   ```

## Endpoints
- `POST /login-with-email-and-password` – Autenticação tradicional.
- `POST /login-with-sso` – Retorna a URL de redirecionamento para login com Google, Microsoft ou GitHub.

## Running Tests 🧪

Use `python -m pytest` to execute the unit tests. The environment variables required by the
application need to be present, and `PYTHONPATH` must include the `src` folder.

```bash
export PYTHONPATH=src
export SUPABASE_URL=http://example.com
export SUPABASE_API_KEY=dummy
export SSO_REDIRECT_TO=http://localhost
python -m pytest
```


## Contributing 🤝
Contributions are welcome! Feel free to open issues or submit pull requests to help improve the project.

---

SupaUser is your go-to solution for modern, scalable user authentication. Enjoy streamlined access control and enhanced security in your applications! 🔒✨
