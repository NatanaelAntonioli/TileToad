## Why and when should I use TileToad? ##

TileToad is a Python application designed to facilitate the creation of terrain tilesets by automatically generating neat transitions between tiles and combinations for cliffs, rivers and waterfalls. 

In a [tile based video game](https://en.wikipedia.org/wiki/Tile-based_video_game) (like the ones made with RPG Maker or 001 Game Creator) the terrain is painted using images (usually square) laid onto the ground referred as tiles. If you don't make transitions between tiles, you'll get a lot of squares. Using transitions, you can make something better, like in the picture bellow. However, making a transition for every combination takes time. 

![](https://i.imgur.com/4BdJj3R.png)

TileToad helps you generating those combinations. It also generates tilesets for cliffs and waterfalls from the same textures. 

![](https://i.imgur.com/kGnQP2f.png)

- [Why and when should I use TileToad?](#why-and-when-should-i-use-tiletoad-)
- [How to run TileToad](#how-to-run-tiletoad)
- [How to generate tilesets](#how-to-generate-tilesets)
- [How tilesets are generated (and how to change that)](#how-tilesets-are-generated--and-how-to-change-that-)
- [FAQ](#faq)
- [Attribution notice](#attribution-notice)

## How to run TileToad ##

You will need [Python 3](https://www.python.org/downloads/). Before running for the first time, you will also need to install [Pillow](https://pillow.readthedocs.io/en/stable/) with `pip install Pillow `

Then all you need to do is to run `tiletoad.py` as you would run any other Python script.

## How to generate tilesets ##

There are 5 input folders you need to worry about when generating tiles. 
The folder `ground` contains all textures for ground tiles (like dirt, grass, sand, pavement or rock).  

![](https://i.imgur.com/9Hk5k8k.png)

The folder `fluid` contains all textures for fluid tiles. By fluid, I mean anything that flows or used to flow (like water, ice or lava). 

![](https://i.imgur.com/N3IZKxO.png)

The folder `rut` contains textures for rut tiles, that will be used to make small cliffs between fluids and ground tiles.

![](https://i.imgur.com/VTCkJ7A.png)

The folder `cliff` contains textures for cliff tiles, that will be used to make the big cliffs.  

![](https://i.imgur.com/OIjbQtl.png)

After you execute the program, it will generate the following assets in their respective folders inside the folder `out`:

`ground-ground` tiles, making the transition between two different ground tiles. Each ground tile is combined with the others, and there are no duplicate combinations
 
![](https://i.imgur.com/rB7Lydh.png) 

`RUT-ground-fluid` tiles, making the transition between a ground and a fluid tile with a small cliff. Each ground tile is combined with each fluid tile. 

![](https://i.imgur.com/gzmj9CU.png)

`BEACH-ground-fluid` tiles, making transition between a ground and a fluid tile without a cliff. Each ground tile is combined with each fluid tile. 

![](https://i.imgur.com/wmpxMyO.png)

`fluid-fluid` tiles, making the transition between two different fluid tiles. Each fluid tile is combined with the others, and there are no duplicate combinations.

![](https://i.imgur.com/8QmcTEP.png)

`cliff` tiles, making the big cliff tiles. Each ground tile is combined with each cliff tile. With the generated sheet, you can make almost any cliff format.

![](https://i.imgur.com/VQDKowl.png)

`stair` tiles, making small tiles for stairs. Each ground tile is combined with each cliff tile.

![](https://i.imgur.com/womNFo5.png)

waterfall tiles, making waterfall and foam tiles. Each fluid tile is used. With the generate sheet, you can make foam in 4 directions, plus full and delimited waterfalls, with special tiles for tops and bottoms. 

![](https://i.imgur.com/7nhB1jD.png)

TileToad will generate a lot of tiles, including some absurd combinations like a smooth frontier between ice and lava. You are not supposed to use every combination, unless you want to.

If you don't want some category of tiles being generated, you can set it to false by editing the header in `tiletoad.py`.

    GENERATE_ground_ground = True
    GENERATE_RUT_fluid_ground = True
    GENERATE_BEACH_fluid_ground = True
    GENERATE_fluid_fluid = True
    GENERATE_cliff = True
    GENERATE_waterfall = True

## How tilesets are generated (and how to change that) ##

That's for advanced users who want to understand how TileToad works or modify the way tiles are generated. If you just want to generate your tiles with custom textures following the default organization, you can skip this section entirely. 

TileToad works mostly by pasting one image on top of another with masks, which are saved in the `masks` folder. White regions means where the image will be preserved. Pink regions are replaced by transparent pixels.

![](https://i.imgur.com/HNWxWNu.png)

The simplest case is for beaches and transitions between two tiles of the same category. TileToad first generates full images for each tiles, and then applies a mask for the top one. Then, the images are pasted on top of another. 

![](https://i.imgur.com/H4RA1Py.png)

The same thing is done for foam.

![](https://i.imgur.com/P6VupFh.png)

When there's a rut, the program will do another iteration for the rut. It will also generate a plain image a little darker than the outer ground, and make a neat contour out of it.

![](https://i.imgur.com/IsQKku9.png)

Generating stairs is very simple, and follows the same logic. 

![](https://i.imgur.com/FbXBdX3.png)

Generating cliffs a bit more complicated, but also follows the same logic. 

![](https://i.imgur.com/rSzRdy2.png)

Generating waterfalls involves making two plain images and composing them to make the falling water effect. It then applies a pink mask to remove some regions and delimit the waterfall contours. 

![](https://i.imgur.com/YQVgLSY.png)

That means you can edit the masks to change how the tilesets will look. Just make sure to study the code and the images before.

## FAQ ##

Not really a FAQ since no one asked me anything yet.

**What is basic size of each tile?**

32x32. For now, this can only be changed by modifying the source code.

**What job TileToad will spare me to do?**

With TileToad, you won't have to worry about manually determining and drawing (or making PhotoShop masks and patterns) for transitions, rivers, cliffs and waterfalls to you game. Just add the base textures, import to your engine and you are good to go.

**Will this tool keep me from manually importing and configuring each transition**?

As of now, no. TileToad only generates the files, and you have to do all the importing and configuration yourself. However, any engine is welcome to implement features that allows auto-importing of TileToad files or even integration with TileToad itself. I'll make sure to add those engines here when they do.

**How can I make tilesets from custom textures?**

Just add them to the corresponding folders, as the rest of the documentation explains. 

**How can I add more tiles and keep the same sequence of generation?**

If you plan on adding more tiles over time, make sure the new ones are last in the sources directory. This keeps the order TileToad uses.

**My textures are kinda ugly, repeating themselves. What can I do?**

Make sure the textures used are [seamless](https://plusspec.com/seamless-texture-tileable-texture/).

**How can I keep track of which textures I already imported?**

I think the best way to import the transitions into an engine is to delete already imported tiles from time to time. This keeps you from scrolling forever just to add a single image. If you made a mistake, just run the program again and all the images will be regenerated. 


## Attribution notice ##

Textures used in the demo were taken from [OpenGameArt](http://opengameart.org/) and [Itch.io](http://itch.io), so I must credit the following contributors:

- [qubodup, Bart K., Blarumyrran](https://opengameart.org/content/oga-community-tileset-nature)
- [Ivan Voirol](https://opengameart.org/content/basic-map-32x32-by-ivan-voirol)
- [Hyptosis](https://opengameart.org/content/lots-of-free-2d-tiles-and-sprites-by-hyptosis)
- ["[LPC] Terrains" by bluecarrot16, Lanea Zimmerman (Sharm), Daniel Eddeland (Daneeklu), Richard Kettering (Jetrel), Zachariah Husiar (Zabin), Hyptosis, Casper Nilsson, Buko Studios, Nushio, ZaPaper, billknye, William Thompson, caeles, Redshrike, Bertram, and Rayane Félix (RayaneFLX)](https://opengameart.org/content/lpc-terrains)
- [Catalin Pavel](https://opengameart.org/content/dirt-texture-pack)
- [PIPOYA](https://pipoya.itch.io/pipoya-rpg-tileset-32x32)

If you decide to use those textures in your game, you'll also have to credit them.
