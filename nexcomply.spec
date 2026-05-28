# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

hiddenimports = collect_submodules("streamlit")
datas = collect_data_files("streamlit")

datas += [
    ("app.py", "."),
    ("config.yaml", "."),
    ("config.toml", "."),
    ("Nexcomplylogo.png", "."),
    ("modules", "modules"),
    ("pages", "pages"),
    ("Frameworks", "Frameworks"),
    ("New Format Policy Docs", "New Format Policy Docs"),
    ("Dummy KL", "Dummy KL"),
    ("Questionnaires", "Questionnaires"),
    ("data", "data"),
]


a = Analysis(
    ["nexcomply_launcher.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="Nexcomply",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
