from PIL import Image

image = Image.open("chess_pieces/png/white_rook.png")
bg = Image.new('RGBA', image.size, 'white')
bg.paste(image, (0,0), image)