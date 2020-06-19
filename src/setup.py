import cx_Freeze

executables = [cx_Freeze.Executable("src/main.py")]

cx_Freeze.setup(
    name="Corona Videogame",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                ("src/images/","images","src/Car.py","src/Player.py")
            ]
        }
    },
    executables=executables
)