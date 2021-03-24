# I love sand. It's smooth and warm and nice, and you can build things out of it

# Dependencies
# It needs you to run pip install Pillow before in order to work.

from tiletools import *
import os
import time

# Use the above variables to configure the program execution.

GENERATE_ground_ground = True
GENERATE_RUT_fluid_ground = True
GENERATE_BEACH_fluid_ground = True
GENERATE_fluid_fluid = True
GENERATE_cliff = True
GENERATE_waterfall = True

# ---------------------- CONSTANTS -----------------------

# Directories

ground_dir = r'ground'
fluid_dir = r'fluid'
rut_dir = r'rut'
cliff_dir = r'cliff'

output_directories = ["out/BEACH-ground-fluid", "out/cliff", "out/ground-ground", "out/fluid-fluid",
                      "out/RUT-ground-fluid", "out/waterfall", "out/stair", ]

# Masks

MASK_ground_ground = 'masks/mask-ground-ground.png'
MASK_fluid_fluid = 'masks/mask-fluid-fluid.png'
MASK_RUT_ground_fluid = 'masks/mask-RUT-ground-fluid.png'
MASK_RUT_ground_fluid2 = 'masks/mask-RUT-ground-fluid2.png'
MASK_reflection = 'masks/mask-reflection.png'
MASK_cliff_background = 'masks/mask-cliff-background.png'
MASK_cliff_material = 'masks/mask-cliff-material.png'
MASK_contour = 'masks/mask-contour.png'
MASK_contour_cliff = 'masks/mask-contour-cliff.png'
MASK_contour_external = 'masks/mask-contour-external.png'
MASK_top_stair = 'masks/mask-top-stair.png'
MASK_contour_stair = 'masks/mask-contour-stair.png'

MASK_waterfall_thin = Image.open('masks/mask-waterfall-thin.png')
MASK_waterfall_left = Image.open('masks/mask-left.png')
MASK_waterfall_right = Image.open('masks/mask-right.png')
MASK_waterfall_top = Image.open('masks/mask-waterfall-top.png')
MASK_waterfall_down = Image.open('masks/mask-waterfall-down.png')

MASK_foam_down = 'masks/mask-foam-down.png'
MASK_foam_up = 'masks/mask-foam-up.png'
MASK_foam_right = 'masks/mask-foam-right.png'
MASK_foam_left = 'masks/mask-foam-left.png'

MASK_waterfall_dark = 'masks/mask-waterfall-dark.png'
MASK_waterfall_middle = 'masks/mask-waterfall-middle.png'
MASK_waterfall_bright = 'masks/mask-waterfall-bright.png'

# Colors

COLOR_transparent = (255, 255, 255, 0)

# Counter

total_tiles = 0


# ---------------------- FUNCTIONS -----------------------

def create_dir():
    for d in output_directories:
        if not os.path.exists(d):
            os.mkdir(d)


def ground_ground():
    global total_tiles
    LIST_ground_ground_done = []  # contains all tiles that have already been combined.

    for ground_tile_current in os.listdir(ground_dir):

        img_ground_tile_current = Image.open(os.path.join(ground_dir, ground_tile_current), 'r')
        background = make_background(img_ground_tile_current, 192.0, 96.0)

        for ground_tile_neigh in os.listdir(ground_dir):

            if (ground_tile_current != ground_tile_neigh) and (ground_tile_neigh in LIST_ground_ground_done):
                img_ground_tile_neigh = Image.open(os.path.join(ground_dir, ground_tile_neigh), 'r')
                neigh = make_background(img_ground_tile_neigh, 192.0, 96.0)
                concat = composite_mask(background, neigh, MASK_ground_ground)

                output = split_image(concat, 1)
                save(output,
                     'out/ground-ground/' + ground_tile_current.replace('.png', '') + '-' + ground_tile_neigh.replace(
                         '.png',
                         '') + '-1.png')
                total_tiles = total_tiles + 1

                output = split_image(concat, 2)
                save(output,
                     'out/ground-ground/' + ground_tile_current.replace('.png', '') + '-' + ground_tile_neigh.replace(
                         '.png',
                         '') + '-2.png')
                total_tiles = total_tiles + 1

        LIST_ground_ground_done.append(ground_tile_current)
        # print(done)


def fluid_fluid():
    global total_tiles

    LIST_fluid_fluid_done = []  # contains all tiles that have already been combined.

    for fluid_tile_current in os.listdir(fluid_dir):

        img_fluid_tile_current = Image.open(os.path.join(fluid_dir, fluid_tile_current), 'r')
        background = make_background(img_fluid_tile_current, 192.0, 96.0)

        for fluid_tile_neigh in os.listdir(fluid_dir):

            if (fluid_tile_current != fluid_tile_neigh) and (fluid_tile_neigh in LIST_fluid_fluid_done):
                img_fluid_tile_neigh = Image.open(os.path.join(fluid_dir, fluid_tile_neigh), 'r')
                neigh = make_background(img_fluid_tile_neigh, 192.0, 96.0)

                concat = composite_mask(background, neigh, MASK_fluid_fluid)

                output = split_image(concat, 1)
                save(output,
                     'out/fluid-fluid/' + fluid_tile_current.replace('.png', '') + '-' + fluid_tile_neigh.replace(
                         '.png',
                         '') + '1.png')
                total_tiles = total_tiles + 1

                output = split_image(concat, 2)
                save(output,
                     'out/fluid-fluid/' + fluid_tile_current.replace('.png', '') + '-' + fluid_tile_neigh.replace(
                         '.png',
                         '') + '2.png')
                total_tiles = total_tiles + 1

        LIST_fluid_fluid_done.append(fluid_tile_current)


def BEACH_fluid_ground():
    global total_tiles

    for fluid_tile_current in os.listdir(fluid_dir):

        img_fluid_tile_current = Image.open(os.path.join(fluid_dir, fluid_tile_current), 'r')
        background = make_background(img_fluid_tile_current, 192.0, 96.0)

        for ground_tile_neigh in os.listdir(ground_dir):
            img_ground_tile_neigh = Image.open(os.path.join(ground_dir, ground_tile_neigh), 'r')
            neigh = make_background(img_ground_tile_neigh, 192.0, 96.0)

            concat = composite_mask(background, neigh, MASK_RUT_ground_fluid)

            output = split_image(concat, 1)
            save(output,
                 'out/BEACH-ground-fluid/' + fluid_tile_current.replace('.png', '') + '-' + ground_tile_neigh.replace(
                     '.png',
                     '') + '-1.png')
            total_tiles = total_tiles + 1

            output = split_image(concat, 2)
            save(output,
                 'out/BEACH-ground-fluid/' + fluid_tile_current.replace('.png', '') + '-' + ground_tile_neigh.replace(
                     '.png',
                     '') + '-2.png')
            total_tiles = total_tiles + 1


def RUT_fluid_ground():
    global total_tiles

    for fluid_tile_current in os.listdir(fluid_dir):

        img_fluid_tile_current = Image.open(os.path.join(fluid_dir, fluid_tile_current), 'r')
        background = make_background(img_fluid_tile_current, 192.0, 96.0)

        for ground_tile_neigh in os.listdir(ground_dir):
            img_ground_tile_neigh = Image.open(os.path.join(ground_dir, ground_tile_neigh), 'r')
            neigh = make_background(img_ground_tile_neigh, 192.0, 96.0)

            for rut_tile in os.listdir(rut_dir):
                img_rut_tile = Image.open(os.path.join(rut_dir, rut_tile), 'r')
                rut = make_background(img_rut_tile, 192.0, 96.0)

                concat1 = composite_mask(background, neigh, MASK_fluid_fluid)

                concat2 = composite_mask(rut, concat1, MASK_RUT_ground_fluid2)

                color_fluid = get_color(img_fluid_tile_current, 16, 16)
                color_ground = get_color(img_ground_tile_neigh, 16, 16)

                painted_fluid = make_painted(color_fluid, 192, 96)
                painted_ground = make_painted(color_ground, 192, 96)

                transparent_background = make_painted(COLOR_transparent, 192, 96)

                reflection = composite_mask(painted_fluid, transparent_background, MASK_reflection)
                reflection = make_brighter(reflection)

                contour = composite_mask(painted_ground, transparent_background, MASK_contour)
                contour = make_darker(contour)

                concat2 = paste_on(concat2, reflection)
                concat2 = paste_on(concat2, contour)

                output = split_image(concat2, 1)
                save(output,
                     'out/RUT-ground-fluid/' + fluid_tile_current.replace('.png', '') + '-' + ground_tile_neigh.replace(
                         '.png',
                         '') + '-' + rut_tile.replace('.png', '') + '-1.png')
                total_tiles = total_tiles + 1

                output = split_image(concat2, 2)
                save(output,
                     'out/RUT-ground-fluid/' + fluid_tile_current.replace('.png', '') + '-' + ground_tile_neigh.replace(
                         '.png',
                         '') + '-' + rut_tile.replace('.png', '') + '-2.png')
                total_tiles = total_tiles + 1


def cliff():
    global total_tiles

    for ground_tile_current in os.listdir(ground_dir):

        img_ground_tile_current = Image.open(os.path.join(ground_dir, ground_tile_current), 'r')
        background = make_background(img_ground_tile_current, 256.0, 256.0)

        for cliff_tile_current in os.listdir(cliff_dir):
            img_cliff_tile_current = Image.open(os.path.join(cliff_dir, cliff_tile_current), 'r')
            cliff_out = make_background(img_cliff_tile_current, 256.0, 256.0)

            transparent = make_painted(COLOR_transparent, 256, 256)

            background = composite_mask(background, transparent, MASK_cliff_background)
            cliff_out = composite_mask(cliff_out, transparent, MASK_cliff_material)

            final = paste_on(background, cliff_out)

            color_ground = get_color(img_cliff_tile_current, 16, 16)

            painted_ground = make_painted(color_ground, 256, 256)

            transparent_background = make_painted(COLOR_transparent, 256, 256)

            contour_cliff = composite_mask(painted_ground, transparent_background, MASK_contour_cliff)
            contour_cliff = make_darker(contour_cliff)

            contour_external = composite_mask(painted_ground, transparent_background, MASK_contour_external)
            contour_external = make_darker(contour_external)

            final = paste_on(final, contour_cliff)
            final = paste_on(final, contour_external)

            save(final, 'out/cliff/' + ground_tile_current.replace('.png', '') + '-' + cliff_tile_current.replace(
                '.png',
                '') + '.png')
            total_tiles = total_tiles + 1

            top_stair = img_ground_tile_current
            cliff_stair = img_cliff_tile_current
            painted_ground = make_painted(color_ground, 32, 32)
            transparent_background = make_painted(COLOR_transparent, 32, 32)

            contour_stair = composite_mask(painted_ground, transparent_background, MASK_contour_stair)

            contour_stair = make_darker(contour_stair)

            final = composite_mask(top_stair, cliff_stair, MASK_top_stair)
            final = paste_on(final, contour_stair)

            save(final, 'out/stair/' + ground_tile_current.replace('.png', '') + '-' + cliff_tile_current.replace(
                '.png',
                '') + '-stair.png')
            total_tiles = total_tiles + 1


def waterfall():
    global total_tiles

    for fluid_tile_current in os.listdir(fluid_dir):
        img_fluid_tile_current = Image.open(os.path.join(fluid_dir, fluid_tile_current), 'r')

        background_fluid = make_background(img_fluid_tile_current, 128, 32)

        background = make_painted(COLOR_transparent, 128, 32)

        color_FLUID = get_color(img_fluid_tile_current, 16, 16)

        color_painted = make_painted(color_FLUID, 128, 32)

        middle = composite_mask(color_painted, background, MASK_waterfall_middle)
        bright = composite_mask(color_painted, background, MASK_waterfall_bright)

        middle = make_brighter(middle)
        bright = make_very_brighter(bright)

        background_fluid = paste_on(background_fluid, middle)
        background_fluid = paste_on(background_fluid, bright)

        waterfall_back = background_fluid.copy()

        waterfall_thin = background_fluid.copy()
        waterfall_left = background_fluid.copy()
        waterfall_right = background_fluid.copy()

        waterfall_left = paste_on(waterfall_left, MASK_waterfall_left)

        waterfall_thin = paste_on(waterfall_thin, MASK_waterfall_thin)

        waterfall_right = paste_on(waterfall_right, MASK_waterfall_right)

        replace_pink_transparent(waterfall_thin)
        replace_pink_transparent(waterfall_left)
        replace_pink_transparent(waterfall_right)

        waterfall_half = get_concat_v(waterfall_back, waterfall_thin)
        waterfall_half = get_concat_v(waterfall_half, waterfall_left)
        waterfall_half = get_concat_v(waterfall_half, waterfall_right)

        waterfall_top = waterfall_half.copy()
        waterfall_down = waterfall_half.copy()

        waterfall_top = paste_on(waterfall_top, MASK_waterfall_top)
        replace_pink_transparent(waterfall_top)

        waterfall_down = paste_on(waterfall_down, MASK_waterfall_down)
        replace_pink_transparent(waterfall_down)

        transparent_background = make_painted(COLOR_transparent, 128, 32)

        background_foam = make_background(img_fluid_tile_current, 128, 32)

        background_foam = make_brighter(background_foam)

        foam_down = composite_mask(background_foam, transparent_background, MASK_foam_down)
        foam_up = composite_mask(background_foam, transparent_background, MASK_foam_up)
        foam_left = composite_mask(background_foam, transparent_background, MASK_foam_left)
        foam_right = composite_mask(background_foam, transparent_background, MASK_foam_right)

        all_foam = get_concat_v(foam_down, foam_up)
        all_foam = get_concat_v(all_foam, foam_right)
        all_foam = get_concat_v(all_foam, foam_left)

        half1 = get_concat_h(waterfall_half, waterfall_top)
        half2 = get_concat_h(waterfall_down, all_foam)

        final = get_concat_v(half1, half2)

        save(final, 'out/waterfall/' + fluid_tile_current.replace('.png', '') + '.png')
        total_tiles = total_tiles + 1


# ---------------------- RUN -----------------------
start_time = time.time()

create_dir()

if GENERATE_ground_ground:
    ground_ground()

if GENERATE_fluid_fluid:
    fluid_fluid()

if GENERATE_BEACH_fluid_ground:
    BEACH_fluid_ground()

if GENERATE_RUT_fluid_ground:
    RUT_fluid_ground()

if GENERATE_cliff:
    cliff()

if GENERATE_waterfall:
    waterfall()

print("")
print("Generated " + str(total_tiles) + " tiles in " + str(round(time.time() - start_time, 2)) + " seconds.")
