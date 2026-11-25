---
title: "SplitKB"
github: ""
description: "Split keyboard from following the guide"
created_at: "2026-11-07"
total_time: "27h 54m"
---

# November 8, 2026: Just followed the tutorial for a bit
<!-- fabricate:entry 2384 -->

Well, as the title says, i followed the tutorial but am thinking of changing it a bit, majorly because i want more keys, and also want to learn ergogen (i will also most probably change the microcontroller for more keys)

![](https://fabricate.hackclub-assets.com/74ce38e75634dc41f078ecf681f6c8db21f334b2c61d55c2acf47284d80824d8/image-png/image.png)

**Total time spent: 3h**

# November 8, 2026 (entry 2): Wiring, getting it wrong, rewiring
<!-- fabricate:entry 2397 -->

Researched on how to make a reversable PCB because why not and it will be cheaper, made the keyboard layout in ergogen, generated it and put it into Kicad, wired everything, forgot i had to wire everything on the flip side too
![](https://fabricate.hackclub-assets.com/0ac2fdc328fedcad38169cb9cd8b933a15c86b41ecd0a7fdf377e1838dccb62f/image-png/image.png)
(this is a new image, i didn't take any screenshots of the wrong one)
wondered why there were 68 errors (34 keys), flipped the footprint, manually rewired it all because i originally didn't take into account the need for wiring it on both sides, rewired it
![](https://fabricate.hackclub-assets.com/ac7e17b0a493c0a421c9547cbfe92abde860f7023dec60dba5601aaea6ac2192/image-png/image.png)
(PS: i used ai to figure out why i was getting the errors after spending half an hour researching with no solution, i suck at researching-)

**Total time spent: 6h 30m**

# November 9, 2026: Fill zones and wiring
<!-- fabricate:entry 2475 -->

![](https://fabricate.hackclub-assets.com/5c2fc3782c55600c1cce0ae5bfcd02a9cd81f2e2e18f918aa7f62c3013919ecc/image-png/image.png)
Created fillzones, connected the switch, added 2 pins for the battery 
![](https://fabricate.hackclub-assets.com/18de7b0aabada219c5d18ff9be1126d7dcf4a7fe61bb6d9a36d92271f4a0d3e9/image-png/image.png)
Time to make the case now, probably gonna use fusion 360 (i deleted it months ago so ill have to go through the hassle of downloading it again)

**Total time spent: 1h**

# November 9, 2026 (entry 2): Mounting holes, PC crshing
<!-- fabricate:entry 2476 -->

Added mounting holes for the PCB, was making the case but after exttrding the z fighting make fusion crash on itself so ill have to do it again-
![](https://fabricate.hackclub-assets.com/05649286a944f9891d8744e66804e555ee323334ddd9e0b940d9275c2ffbee26/image-png/image.png)
(last photo before it going boom boom)

**Total time spent: 30m**

# November 10, 2026: CADding
<!-- fabricate:entry 2551 -->

![](https://fabricate.hackclub-assets.com/9d1f5e6678087655185101785cbbe7506cf1821f8a5309c7427cc3c2e3de92da/image-png/image.png)
Made 3d case models of both the sides (js made one and mirrored it) , decided not to go for the switchplate because it felt redundant (maybe will later) probably gonna ship it soon
Started making the BOM, just rechecking the out of stock items and crosschecking to minimize cost

**Total time spent: 7h**

# November 10, 2026 (entry 2): Finished the carts
<!-- fabricate:entry 2553 -->

Got all the items i need in carts, all i need now is making a BOM and a github page (i couldnt fint he appropriate batteries so i had to get them from a separate place
![](https://fabricate.hackclub-assets.com/9758e0d8016f5dd87ae51a5d4b09698c0e1cc5cb01e44d211bdbe6af2e10c43f/image-png/image.png)
![](https://fabricate.hackclub-assets.com/0d9b938826a4c8695ec1b9efcea8b7b662834714eb3b379a67c0350ac7540f83/image-png/image.png)
![](https://fabricate.hackclub-assets.com/412c5f9ea1a8cebb847b3c3c29d919b243a01214cabb30b7f3ad51715a2c9ad2/image-png/image.png)
![](https://fabricate.hackclub-assets.com/0a3c52ba33a2d34fea18f091421061f4555e961f23d27163067f25fe475a4244/image-png/image.png)

**Total time spent: 1h**

# November 10, 2026 (entry 3): Made Readme, coded firmware
<!-- fabricate:entry 2556 -->

As the title says, i made the firmware in KMK and made the github page for README.md, all i have left to do is to get all my files together and o over the submitting page again
![](https://fabricate.hackclub-assets.com/46ac9bf0d376f020535da28e80761a08cd14d660258b4e93bf334cb21dd3a0d5/image-png/image.png)

**Total time spent: 2h**

# November 14, 2026: Placeholder entry for time spent in the github setup
<!-- fabricate:entry 2988 -->

This entry is soley here to account for the time spent during the git setup along with troubleshooting of the program, (also time spent recovering files because i didnt know --force erases the files which arent on your pc TT)
![](https://fabricate.hackclub-assets.com/74bfc5eaab5f2b27824c5ebf554b205994993dd8a3383fc1dc0c70cf1d4bd3eb/image-png/image.png)

**Total time spent: 1h**

# November 21, 2026: Added BOM.CSV, schematic, Assembly CAD, and polish in readme
<!-- fabricate:entry 3577 -->

![](https://fabricate.hackclub-assets.com/485be4c18bc512ccab0759e0ca86b86ff226f0bb9f96753cbb7d1b3794bb3d79/image-png/image.png)
I made and added a BOM.csv along with making a schematic in KiCad (it took me too long to figure out how to rename untitled to scrappy_pcb2 without it showing errors TT)
fusion crashed multiple times when trying to move multiple keycaps and switches TT so it took me wayy too long than it should have

**Total time spent: 3h 30m**

# November 21, 2026 (entry 2): Im dumb TT
<!-- fabricate:entry 3590 -->

well guess what happened, IM DUMBBBBBBBB (i didnt recheck the assembly and just realized that meshes do not show up, and guess what)
![](https://fabricate.hackclub-assets.com/3eb617a03b8ca0d83110f3aad4de6ba28367ccd3c95aae4b22121b2b9c2f6d77/image-png/image.png)
my PC has crashed about 3 times trying to do this, wish me luck

**Total time spent: 2h**

# November 21, 2026 (entry 3): Just made it a .stl file
<!-- fabricate:entry 3598 -->

so i gave up and settled for just making it a .stl file
![](https://fabricate.hackclub-assets.com/cba378f21b1153d2d7dbcd9781a304bdb1c926ddbb88764f44a7a3cf89c6f041/image-png/image.png)
it is like, 54 MB but afaik it shouldnt really be a concern, im probably gonna rest now, or work on another project, im tiredd TT

**Total time spent: 18m**

# November 25, 2026: Clarification on Assembeled CAD model
<!-- fabricate:entry 3874 -->

The assembled file should be located in ScrappyKB-main\CAD\Assembeled.stl
![](https://fabricate.hackclub-assets.com/f93e5be230439f3554994443cd491a3427423de46f77914a28977ea8d647c69d/image-png/image.png)
But i will rebuild the files as i will probably modify it a bit (i want to make the switch plate bigger)
I am assuming the for the assembly a .step file is necessary, so wish me luck TT

![](https://fabricate.hackclub-assets.com/d5a4ec6da69f8078f231b36c4c41270e0cf336f36900e299ce1096c5fbd185c3/image-png/image.png)

nevermind TT
![](https://fabricate.hackclub-assets.com/a673d22a9434b03dac97d370400c614b08cab3309712996841642b515d97645d/image-png/image.png)

**Total time spent: 6m**
