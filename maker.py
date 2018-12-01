import os
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from slugify import slugify

catalog = {
    'releases': [
        #{
        #    'catalog': 'POLAAR-001',
        #    'artist': 'Flore',
        #    'name': 'RITUAL Part 1',
        #    'cover': '/Users/marc/POLAAR/Releases/POLAAR-006 – Drumyard Part 1 (Tim Karbon)/drumyard1-2.png',
        #    'tracks': [
        #        { 'artist': 'Flore', 'name': 'Numen'},
        #        { 'artist': 'Flore', 'name': 'Random'},
        #        { 'artist': 'Flore', 'name': 'Graved On Stone'},
        #    ]
        #},
        #{
        #    'catalog': 'POLAAR-002',
        #    'artist': 'Flore',
        #    'name': 'RITUAL Part 2',
        #    'cover': '/Users/marc/POLAAR/Releases/POLAAR-006 – Drumyard Part 1 (Tim Karbon)/drumyard1-2.png',
        #    'tracks': [
        #        { 'artist': 'Flore', 'name': 'Attack Me'},
        #        { 'artist': 'Flore', 'name': 'Blood'},
        #        { 'artist': 'Flore', 'name':'Psykhe'},
        #    ]
        #},
        #{
        #    'catalog': 'POLAAR-003',
        #    'artist': 'Various Artists',
        #    'name': 'Territoires Vol. 1',
        #    'cover': '/Users/marc/POLAAR/Releases/POLAAR-006 – Drumyard Part 1 (Tim Karbon)/drumyard1-2.png',
        #    'tracks': [
        #        { 'artist': 'Prettybwoy', 'name':'Hansei'},
        #        { 'artist': 'Hoodrat', 'name':'Car Crash'},
        #        { 'artist': 'SNKLS', 'name':'Isandula'},
        #        { 'artist': 'Prettybwoy', 'name': 'Untitled 0611'},
        #        { 'artist': 'SNKLS', 'name': 'Hemera'},
        #        { 'artist': 'Hoodrat', 'name': 'U'},
        #    ]
        #},
        #{
        #    'catalog': 'POLAAR-004',
        #    'artist': 'Prettybwoy',
        #    'name': 'Overflow EP',
        #    'cover': '/Users/marc/POLAAR/Releases/POLAAR-006 – Drumyard Part 1 (Tim Karbon)/drumyard1-2.png',
        #    'tracks': [
        #        { 'artist': 'Prettybwoy', 'name':'Overflow'},
        #        { 'artist': 'Prettybwoy', 'name':'Vivid Colour'},
        #        { 'artist': 'Prettybwoy', 'name':'Humid'},
        #        { 'artist': 'Prettybwoy', 'name':'Flutter'},
        #    ]
        #},
        #{
        #    'catalog': 'POLAAR-005',
        #    'artist': 'Only Now',
        #    'name': 'Elements',
        #    'cover': '/Users/marc/POLAAR/Releases/POLAAR-006 – Drumyard Part 1 (Tim Karbon)/drumyard1-2.png',
        #    'tracks': [
        #        { 'artist': 'Only Now', 'name':'Dirt'},
        #        { 'artist': 'Only Now', 'name':'Factory Ghost'},
        #        { 'artist': 'Only Now', 'name':'Elements'},
        #        { 'artist': 'Only Now', 'name':'Tribute To Detroit'},
        #    ]
        #},
        {
            'catalog': 'POLAAR-006',
            'artist': 'Tim Karbon',
            'name': 'Drumyard Part 1',
            'cover': '/Users/marc/POLAAR/Releases/POLAAR-006 – Drumyard Part 1 (Tim Karbon)/drumyard1-2.png',
            'tracks': [
                { 'artist': 'Tim Karbon', 'name':'Aziz Lumière'},
                { 'artist': 'Tim Karbon', 'name':'For The Birds'},
                { 'artist': 'Tim Karbon', 'name':'Loud Poetry'},
                { 'artist': 'Tim Karbon', 'name':'Decelerate Oasis'},
            ]
        },
        {
            'catalog': 'POLAAR-007',
            'artist': 'Prettybwoy',
            'name': 'Parallel Lives',
            'cover': '/Users/marc/POLAAR/Releases/POLAAR-007 - Prettybwoy/2. cover/cover.jpg',
            'tracks': [
                { 'artist': 'Prettybwoy', 'name':'Oculoagravic'},
                { 'artist': 'Prettybwoy', 'name':'Simulacre'},
                { 'artist': 'Prettybwoy', 'name':'The Shelter'},
            ]
        },
        {
            'catalog': 'POLAAR-008',
            'artist': 'Mars89 & KEITO',
            'name': '4G',
            'cover': '/Users/marc/POLAAR/Releases/POLAAR-008 Mars89 KΣITO Gqom split/2. cover/cover-3000x3000.png',
            'tracks': [
                { 'artist': 'KEITO', 'name':'Bougainvillea', 'wav': '/Users/marc/POLAAR/Releases/POLAAR-008 Mars89 KΣITO Gqom split/Masters/Keito Masters 2 Pack/Around -10/17070901Gqom master 2 48 24 -10.7 dB LUFS.wav' },
                { 'artist': 'KEITO', 'name':'9th Floor', 'wav': '/Users/marc/POLAAR/Releases/POLAAR-008 Mars89 KΣITO Gqom split/Masters/Keito Masters 2 Pack/Around -10/18101601gqom master 2 48 24 -10.6 dB LuFs.wav'},
                { 'artist': 'Mars89', 'name':'Hydrophobia', 'wav': '/Users/marc/POLAAR/Releases/POLAAR-008 Mars89 KΣITO Gqom split/Masters/Mars89 Masters 2 Pack/Around -11/Hydrphobia master 2 48 24 -11 dB LuFs.wav'},
                { 'artist': 'Mars89', 'name':'Sky Burial', 'wav': '/Users/marc/POLAAR/Releases/POLAAR-008 Mars89 KΣITO Gqom split/Masters/Mars89 Masters 2 Pack/Around -11/Sky Burial master 2 48 24 -11 dB LuFs.wav'}
            ]
        }
    ]
}

# release information
coverOriginal = '4g.png'

font = 'NeutraText-Book.otf'
polaar = Image(filename='polaar-logo-white-2014.png')
cover = Image(filename=coverOriginal)

def image_square_for_video(track: str, artist: str, cover: Image, logo: Image, path: str):
    with Drawing() as draw:
        height=1080
        width=1080
        logoClone = logo.clone()
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
        draw.text(width // 2, int(height * 0.79), track)
        draw.font_size = 48
        draw.text(width // 2, int(height * 0.84), artist)
        draw.font_size = 36
        draw.text(width // 2, int(height * 0.95), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s/%s_%s_square.png' % (path, slugify(artist), slugify(track)))

def image_portrait_for_video(track: str, artist: str, cover: Image, logo: Image, path: str):
    with Drawing() as draw:
        height=1280
        width=720
        logoClone = logo.clone()
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
        draw.text(width // 2, int(height * 0.59), track)
        draw.font_size = 48
        draw.text(width // 2, int(height * 0.63), artist)
        draw.font_size = 36
        draw.text(width // 2, int(height * 0.76), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s/%s_%s_portrait.png' % (path, slugify(artist), slugify(track)))

def image_landscape_for_video(track: str, artist: str, cover: Image, logo: Image, path: str):
    with Drawing() as draw:
        width=1280
        height=720
        logoClone = logo.clone()
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
        draw.text(width // 2, int(height * 0.21), track)
        draw.font_size = 48
        draw.text(width // 2, int(height * 0.28), artist)
        draw.font_size = 36
        draw.text(width // 2, int(height * 0.86), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s/%s_%s_landscape.png' % (path, slugify(artist), slugify(track)))

def image_landscape_for_facebook(release: str, artist: str, cover: Image, logo: Image, path: str):
    with Drawing() as draw:
        width=851
        height=315
        logoClone = logo.clone()
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
        draw.text(int(width * 0.663), int(height * 0.21), release)
        draw.font_size = 36
        draw.text(int(width * 0.663), int(height * 0.35), artist)
        draw.font_size = 18
        draw.text(int(width * 0.663), int(height * 0.56), 'Available now, everywhere')
        draw(result)
        result.format = 'png'
        result.save(filename='%s/%s-facebook.png' % (path, slugify(release)))

for release in catalog['releases']:
    path = 'out/%s_%s_%s' % (slugify(release['catalog']), slugify(release['artist']), slugify(release['name']))
    if not os.path.isdir(path):
        os.mkdir(path)

    cover = Image(filename=release['cover'])
    image_landscape_for_facebook(release['name'], release['artist'], cover, polaar, path)
    for track in release['tracks']:
        image_square_for_video(track['name'], track['artist'], cover, polaar, path)
        image_portrait_for_video(track['name'], track['artist'], cover, polaar, path)
        image_landscape_for_video(track['name'], track['artist'], cover, polaar, path)
