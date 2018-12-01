from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# release information
font = 'NeutraText-Book.otf'
release = {'artist': 'Mars89 & KEITO', 'name': '4G'}
tracks = [
    {'artist': 'KEITO', 'track':'Bougainvillea'},
    {'artist': 'KEITO', 'track':'9th Floor'},
    {'artist': 'Mars89', 'track':'Hydrophobia'},
    {'artist': 'Mars89', 'track':'Sky Burial'}
]
coverOriginal = '4g.png'

polaar = Image(filename='polaar-logo-white-2014.png')
cover = Image(filename=coverOriginal)

def image_square_for_video():
    with Drawing() as draw:
        height=1080
        width=1080
        logoClone = polaar.clone()
        logoClone.resize(130, 130)
        clone = cover.clone()
        clone.resize(int(height * 0.6), int(width * 0.6))
        result = Image(width=1080, height=1080, background=Color('black'))
        result.composite(logoClone, int(width * 0.84), int(height * 0.84))
        result.composite(clone, int(width * 0.2), int(height * 0.1))
        draw.fill_color = Color('white')
        draw.font = font
        draw.text_antialias = True
        draw.text_alignment = 'center'
        draw.font_size = 64
        draw.text(width // 2, int(height * 0.79), tracks[0]['track'])
        draw.font_size = 48
        draw.text(width // 2, int(height * 0.84), tracks[0]['artist'])
        draw.font_size = 36
        draw.text(width // 2, int(height * 0.95), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s-%s-square.png' % (tracks[0]['artist'], tracks[0]['track']))

def image_portrait_for_video():
    with Drawing() as draw:
        height=1280
        width=720
        logoClone = polaar.clone()
        logoClone.resize(130, 130)
        clone = cover.clone()
        clone.resize(576, 576)
        result = Image(width=width, height=height, background=Color('black'))
        result.composite(logoClone, int(width * 0.41), int(height * 0.85))
        result.composite(clone, int(width * 0.10), int(height * 0.05))
        draw.fill_color = Color('white')
        draw.font = font
        draw.text_antialias = True
        draw.text_alignment = 'center'
        draw.font_size = 64
        draw.text(width // 2, int(height * 0.59), tracks[0]['track'])
        draw.font_size = 48
        draw.text(width // 2, int(height * 0.63), tracks[0]['artist'])
        draw.font_size = 36
        draw.text(width // 2, int(height * 0.76), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s-%s-portrait.png' % (tracks[0]['artist'], tracks[0]['track']))

def image_landscape_for_video():
    with Drawing() as draw:
        width=1280
        height=720
        logoClone = polaar.clone()
        logoClone.resize(130, 130)
        clone = cover.clone()
        clone.resize(512, 512)
        result = Image(width=width, height=height, background=Color('black'))
        result.composite(clone, int(width * 0.05), int(height * 0.15))
        result.composite(logoClone, int(width * 0.85), int(height * 0.695))
        draw.fill_color = Color('white')
        draw.font = font
        draw.text_antialias = True
        draw.text_alignment = 'left'
        draw.font_size = 64
        draw.text(width // 2, int(height * 0.21), tracks[0]['track'])
        draw.font_size = 48
        draw.text(width // 2, int(height * 0.28), tracks[0]['artist'])
        draw.font_size = 36
        draw.text(width // 2, int(height * 0.86), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s-%s-landscape.png' % (tracks[0]['artist'], tracks[0]['track']))

def image_landscape_for_facebook():
    with Drawing() as draw:
        width=851
        height=315
        logoClone = polaar.clone()
        logoClone.resize(64, 64)
        clone = cover.clone()
        clone.resize(253, 253)
        result = Image(width=width, height=height, background=Color('black'))
        result.composite(clone, int(width * 0.075), int(height * 0.10))
        result.composite(logoClone, int(width * 0.625), int(height * 0.701))
        draw.fill_color = Color('white')
        draw.font = font
        draw.text_antialias = True
        draw.text_alignment = 'center'
        draw.font_size = 48
        draw.text(int(width * 0.663), int(height * 0.21), release['name'])
        draw.font_size = 36
        draw.text(int(width * 0.663), int(height * 0.35), release['artist'])
        draw.font_size = 18
        draw.text(int(width * 0.663), int(height * 0.56), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s-facebook.png' % (release['name']))


#image_square_for_video()
#image_portrait_for_video()
#image_landscape_for_video()
image_landscape_for_facebook()
