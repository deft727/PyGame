# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\hp\\Desktop\\pygame'],
             binaries=[],
             datas=[
                 ('sounds/bird.mp3','sounds'),
                 ('sounds/po.w64','sounds'),
                 ('sounds/ahr.w64','sounds'),
                 ('images/score_fon.png','images'),

                 ('images/telega.png','images'),
                 ('images/Thngs-1.png','images'),
                 ('images/Thngs-2.png','images'),
                 ('images/Thngs-3.png','images'),
                 ('images/Thngs-7.png','images'),
                 ('images/Thngs-13.png','images'),
                 ('images/Thngs-17.png','images'),
                 ('images/Thngs-19.png','images'),
                  ('images/Thngs-26.png','images')
                  
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
