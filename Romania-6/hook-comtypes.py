# hook-comtypes.py

from PyInstaller.utils.hooks import copy_metadata, collect_submodules

datas = copy_metadata('comtypes')
hiddenimports = collect_submodules('comtypes')
