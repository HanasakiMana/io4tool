# -*- mode: python ; coding: utf-8 -*-


a = Analysis([
    'main.py',
    'const.py',
    'GUI.py',
    'hid.py',
    'IO.py'
    ],
    pathex=[],
    binaries=[],
    datas=[
        ('favicon.ico', '.'),
        ('lib/libhidapi.dylib', 'lib')
        ],
    hiddenimports=[],
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
    name='IO4Tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.ico'],
)

app = BUNDLE(exe,
        name='IO4Tool.app',
        icon='icon.icns',
        bundle_identifier=None,
        version='1.1',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            'CFBundleDocumentTypes': [
                {
                    'CFBundleTypeName': 'IO4Tool',
                    'CFBundleTypeIconFile': 'icon.icns',
                    'LSItemContentTypes': ['com.mana.io4tool']
                }
            ]
        },
    )
