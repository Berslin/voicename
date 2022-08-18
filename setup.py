import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voice_traile",
    #version="1.0.4",
    description="Singing synthesis from MIDI file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Berslin/voice_traile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "music21", "Pyphen"],
    python_requires='>=3.6',
)
