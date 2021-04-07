# Dependencies
# It needs you to run pip install Pillow before in order to work.

from PIL import Image, ImageEnhance
import math

# ---------------------- CONSTANTS AND COUNTERS -----------------------

mask_dir = r'masks'


# ---------------------- FUNCTIONS -----------------------

# Concatenates two images horizontally.
def get_concat_h(im1, im2):
    dst = Image.new('RGBA', (im1.width + im2.width, im1.height), (255, 0, 0, 0))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


# Concatenates two images vertically.
def get_concat_v(im1, im2):
    dst = Image.new('RGBA', (im1.width, im1.height + im2.height), (255, 0, 0, 0))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


# Uses an image the size of img and creates another image the size of height x width by repeating img.
def make_background(img, width, height):
    img_single = img
    final = img

    for horizontal in range(math.floor((width / img.width) - 1)):
        final = get_concat_h(final, img_single)

    img_line = final

    for vertical in range(math.floor((height / img.height) - 1)):
        final = get_concat_v(final, img_line)

    return final


# Composites two im1 on im2 applying mask
def composite_mask(im1, im2, mask):
    img_mask = Image.open(mask).convert('L')
    final = Image.composite(im1, im2, img_mask)

    return final


# Splits vertically im (128x96) in two. part = 1 returns the first half, and part = 2 returns the second half
def split_image(im, part):
    box1 = (0, 0, 96, 96)
    box2 = (96, 0, 192, 96)

    if part == 1:
        final = im.crop(box1)
    else:
        final = im.crop(box2)

    return final


# Pastes one image on top of another
def paste_on(im1, im2):
    im1.paste(im2, (0, 0), im2)
    return im1


# Pastes one image on top of another using alpha
def paste_alpha(background, foreground):
    return Image.alpha_composite(background, foreground)


# Gets color from a im1 pixel
def get_color(im, width, height):
    pix = im.load()
    return pix[width, height]


# Creates an image width x height with the color color.
def make_painted(color, width, height):
    return Image.new('RGBA', (width, height), color)


# Makes an image brighter
def make_brighter(im):
    enhancer = ImageEnhance.Brightness(im)

    im_output = enhancer.enhance(1.4)

    return im_output


# Makes an image dimmer
def make_darker(im):
    enhancer = ImageEnhance.Brightness(im)

    im_output = enhancer.enhance(0.7)

    return im_output


# Makes an image very brighter
# Go horse is not nice. But if you are here for riddles: https://bit.ly/39TmvBv
def make_very_brighter(im):
    enhancer = ImageEnhance.Brightness(im)

    im_output = enhancer.enhance(1.6)

    return im_output


# Replaces every pink pixel (255, 0, 234,255) with a transparent one.
def replace_pink_transparent(img):
    pixels = img.load()  # create the pixel map

    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            if pixels[i, j] == (255, 0, 234, 255):
                # change to black if not red
                pixels[i, j] = (0, 0, 0, 0)


# Saves an image
def save(image, name):
    image.save(name)
    print("Saved " + name)
