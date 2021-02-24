from distutils.core import setup
import py2exe

setup(
    name="A BioShock-Themed Treasure Hunting Game",
    license="MIT",
    console=[{"script": "play.py", "icon_resources": [(0, "icon.ico")]}],
    packages=["modules"],
)
