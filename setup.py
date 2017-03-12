from cx_Freeze import setup, Executable

setup(
    name = "Fb poster Gelfandrealty",
    version = "0.2",
    description = "Fb poster Gelfandrealty",
    executables = [Executable("main.py")]
)
