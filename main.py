import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

W, H = 640, 360

def openImage(path):
    im = Image.open(path)
    im.show()

def createCharacters(path, character1, character2):
    # First character image
    character1Image = Image.open(path + '/' + character1 + '.png')
    
    # Second character image
    character2Image = Image.open(path + '/' + character2 + '.png')

    # Compute new size
    baseWidth = 196
    size = (baseWidth, int(baseWidth * character1Image.size[1] / character1Image.size[0]))
    
    # Resize images
    character1Image = character1Image.resize(size, Image.ANTIALIAS)
    character2Image = character2Image.resize(size, Image.ANTIALIAS)

    # Return images
    return character1Image, character2Image


def pasteCharacterImages(image, character1, character2):
    # Mirror character 2
    character2 = ImageOps.mirror(character2)

    # Paste characters
    image.paste(character1, (0, 54), character1) 
    image.paste(character2, (W - character2.size[0], 54), character2)


def writePlayers(fontPath, image, player1, player2):
    # Load font
    font = ImageFont.truetype(fontPath, 40)
    
    # Drawing context
    draw = ImageDraw.Draw(image)

    # Init widths
    w1 = draw.textsize(player1, font=font)[0]
    w2 = draw.textsize(player2, font=font)[0]

    # Compute starting coordinates
    x1 = W / 4 - w1 / 2
    x2 = 3 * W / 4 - w2 / 2

    # Draw players tags
    draw.text((x1, 4), player1, font=font, fill=(255,255,255,255))
    draw.text((x2, 4), player2, font=font, fill=(255, 255, 255, 255))

def writeTournament(fontPath, image, name):
    # Load font
    font = ImageFont.truetype(fontPath, 36)
    
    # Drawing context
    draw = ImageDraw.Draw(image)

    # Init width
    w = draw.textsize(name, font=font)[0]

    # Draw players tags
    draw.text(((W - w) / 2, H - 42), name, font=font, fill=(255, 255, 255, 255))

def writeRound(fontPath, image, name):
    # Load font
    font = ImageFont.truetype(fontPath, 32)
    
    # Drawing context
    draw = ImageDraw.Draw(image)

    # Init width
    w = draw.textsize(name, font=font)[0]

    # Draw players tags
    draw.text(((W - w) / 2, 3 * H / 5), name, font=font, fill=(255,255,255,255))


if __name__ == '__main__':
    print('SSBM Youtube Thumbnail Generator')
    if (len(sys.argv) == 10):
        # Parse arguments
        fontPath = sys.argv[1]
        spritesFolderPath = sys.argv[2]
        tournamentName = sys.argv[3]
        roundName = sys.argv[4]
        player1 = sys.argv[5]
        player2 = sys.argv[6]
        character1 = sys.argv[7]
        character2 = sys.argv[8]
        output = sys.argv[9]

        # Print arguments
        print('Font path: ' + fontPath)
        print('Sprites folder: ' + spritesFolderPath)
        print(tournamentName + ' - ' + roundName)
        print(player1 + ' - ' + character1)
        print(player2 + ' - ' + character2)

        # Init image with background
        image = Image.new('RGBA', (W, H), 'black')

        # Open character images
        character1Image, character2Image = createCharacters(spritesFolderPath, character1, character2)

        # Paste character images
        pasteCharacterImages(image, character1Image, character2Image)

        # Write players tags
        writePlayers(fontPath, image, player1, player2)

        # Write tournament name
        writeTournament(fontPath, image, tournamentName)

        # Write round name
        writeRound(fontPath, image, roundName)

        # Save image
        image.save(output)
    else:
        print('Arguments: [font name] [sprites folder path] ' +
            '[tournament name] [round name] ' +
            '[player 1] [player2] [character 1] [character 2]' +
            '[output file]'
        )