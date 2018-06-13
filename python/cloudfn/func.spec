# -*- mode: python -*-

block_cipher = None


a = Analysis(['../main.py'],
             pathex=['../', '/Users/li_qun_tang/Documents/Github/tut-gcloud/python/cloudfn'],
             binaries=[],
             datas=[],
             hiddenimports=['htmlentitydefs', 'HTMLParser', 'Cookie'],
             hookspath=['/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cloudfn/hooks'],
             runtime_hooks=['/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cloudfn/hooks/unbuffered.py'],
             excludes=['jinja2.asyncsupport', 'jinja2.asyncfilters'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='func',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='func')
