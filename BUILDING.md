# Building Nexcomply Windows executable (.exe)

## Prerequisites (Windows 10/11)

- Python 3.10
- pip

## 1) Install dependencies

From the repository root:

```powershell
pip install -r requirements.txt
pip install pyinstaller==6.11.1
```

## 2) Build the executable

```powershell
pyinstaller --noconfirm --clean nexcomply.spec
```

Output executable:

- `dist\\Nexcomply.exe`

## 3) Run the app

```powershell
.\dist\Nexcomply.exe
```

When started, Streamlit serves the app locally (default: <http://localhost:8501>). Open that URL in your browser if it does not open automatically.

## GitHub Actions artifact

A workflow at `.github/workflows/windows-exe.yml` builds the `.exe` on `windows-latest` and uploads:

- `nexcomply-windows-exe` artifact containing `Nexcomply.exe`

You can download it from the Actions run summary for pushes/tags.
