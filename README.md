# doordash-multilogin

Python automation tooling that integrates browser profiles (Multilogin) with DoorDash-related workflows. This repository is intended for learning how Selenium-style automation and external SMS/image APIs are wired together—not as a production service.

## Disclaimer

This project is provided for **educational and research purposes only**.

- Use at your own risk. The authors are not responsible for misuse, account bans, or legal consequences.
- Automated access may violate third-party terms of service (DoorDash, SMS providers, image APIs, and others).
- Do not use this software for spam, fraud, harassment, or any activity that causes harm.

## Requirements

- Python 3.x (see `requirements.txt`)
- Chrome / Chromedriver or undetected-chromedriver as configured in the project
- Optional: Multilogin local API when running in production mode

## Setup

1. Clone the repository and create a virtual environment:

   ```bash
   git clone https://github.com/fineanmol/doordash-multilogin.git
   cd doordash-multilogin
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Copy the example config and fill in your own values locally (never commit `config.ini`):

   ```bash
   cp config.ini.example config.ini
   ```

3. Set API keys via environment variables (recommended) or edit `config.ini`:

   | Variable | Purpose |
   |----------|---------|
   | `SMSPOOL_API_KEY` | SMS Pool API key |
   | `PEXELS_API_KEY` | Pexels API authorization key |
   | `ENVIRONMENT` | Config section name: `Local` (default) or `Prod` |

   Example:

   ```bash
   export SMSPOOL_API_KEY="your-smspool-key"
   export PEXELS_API_KEY="your-pexels-key"
   export ENVIRONMENT=Local
   ```

4. Run the entrypoint (see `main.py` for CLI usage):

   ```bash
   python main.py
   ```

## Configuration

- `config.ini.example` — committed template with placeholder values.
- `config.ini` — local-only file (gitignored). Keys in the file are used only when the corresponding environment variable is unset.

## License

GPL-3.0 — see [LICENSE](LICENSE).
