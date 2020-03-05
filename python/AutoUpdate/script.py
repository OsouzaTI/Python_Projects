from cx_Freeze import setup, Executable

setup(name='GUIupdate',
    version='1.0',
    description='Software for updates',
    options={'build_exe': {'packages': ['matplotlib']}},
    executables = [Executable(
                       script='GUIupdate.py',
                       base="Win32GUI",
                       icon='logo.ico',                       
                       )
                  ]      
)
