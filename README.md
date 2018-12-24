# SSBM Youtube Thumbnail Generator

![Demo](http://image.noelshack.com/fichiers/2018/52/1/1545658965-foxadb.png)

## Requirements

- Python 3.x
- Pillow: ``pip install Pillow``

## Usage

Prepare your font file (OTF and TTF formats supported) and your sprite folder containing the characters png files (e.g. ``fox.png``, ``marth.png``, etc)

```
python main.py [font file] [sprite folder] [tournament] [round] [player 1] [player 2] [character 1] [character 2] [output file]
```

Example:
```
python main.py example/font/impact.ttf example/sprite 'MELTDOWN GRENOBLE #3' 'LOSER R6' 'FOXADB' 'TOUFFE' fox samus image.png
```
