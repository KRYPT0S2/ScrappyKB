---
title: "SplitKB"
github: "https://github.com/KRYPT0S2/ScrappyKB"
description: "A custom 68-key wireless split keyboard made with Ergogen, KiCad, Fusion 360, and KMK firmware."
created_at: "2026-11-07"
total_time: "28h 54m"
---

# November 8, 2026: Just followed the tutorial for a bit
<!-- fabricate:entry 2384 -->

Well, as the title says, i followed the tutorial but am thinking of changing it a bit, majorly because i want more keys, and also want to learn ergogen (i will also most probably change the microcontroller for more keys). i also landed on using KMK firmware because it is relatively easier to use along with me already knowing the basics of it.

![](https://fabricate.hackclub-assets.com/74ce38e75634dc41f078ecf681f6c8db21f334b2c61d55c2acf47284d80824d8/image-png/image.png)

**Total time spent: 3h**

# November 8, 2026 (entry 2): Wiring, getting it wrong, rewiring
<!-- fabricate:entry 2397 -->

I looked up how to make the PCB reversible because ordering one 5 pack of PCBs from JLCPCB that works for both the left and right halves is wayyy cheaper than ordering two separate boards. I wrote the layout in Ergogen, generated the PCB, opened it in KiCad, and wired it up.

When I ran DRC, it threw 68 errors (Two for every switch) because I forgot that flipping the board for the other hand changes which side the Pro Micro pins sit on so it needs wires on both sides TT. I ended up flipping the microcontroller footprint, figuring out how the mirrored pins line up, and manually rewiring both sides of the matrix so that everything connects properly no matter which way you flip the PCB.

![](https://fabricate.hackclub-assets.com/0ac2fdc328fedcad38169cb9cd8b933a15c86b41ecd0a7fdf377e1838dccb62f/image-png/image.png)
![](https://fabricate.hackclub-assets.com/ac7e17b0a493c0a421c9547cbfe92abde860f7023dec60dba5601aaea6ac2192/image-png/image.png)

**Total time spent: 6h 30m**

# November 9, 2026: Fill zones and wiring
<!-- fabricate:entry 2475 -->

Once the key matrix was finally done, I added the on/off switch and battery connections. I placed an MSK12C02-HB slide switch and two battery pads so each half can run off a 3.7V 300mah LiPo battery and be turned completely off when I'm not using it. Then I poured GND copper fill zones across the front and back of the PCB so all the ground pins connect cleanly, and started setting up Fusion 360 to make the case.

![](https://fabricate.hackclub-assets.com/5c2fc3782c55600c1cce0ae5bfcd02a9cd81f2e2e18f918aa7f62c3013919ecc/image-png/image.png)
![](https://fabricate.hackclub-assets.com/18de7b0aabada219c5d18ff9be1126d7dcf4a7fe61bb6d9a36d92271f4a0d3e9/image-png/image.png)

**Total time spent: 1h**

# November 9, 2026 (entry 2): Mounting holes, PC crshing
<!-- fabricate:entry 2476 -->

I added four M2 mounting holes around the edges of the PCB in KiCad and exported the board shape into Fusion 360. While trying to extrude the case walls directly from the imported board faces, well it crashed Fusion 360 before I could save TT, so I had to start over. Atleast i finally finished the case

![](https://fabricate.hackclub-assets.com/05649286a944f9891d8744e66804e555ee323334ddd9e0b940d9275c2ffbee26/image-png/image.png)

**Total time spent: 30m**

# November 10, 2026: CADding
<!-- fabricate:entry 2551 -->

After restarting the sketch, I modeled tray case for the left half, cutouts for the USB C port and power switch, and 1.8mm screw standoffs so the screws can thread into the plastic. I also designed a 1.5mm switch plate with 5mm spacers, then mirrored the whole case and plate for the right half. At the same time, I started checking local Indian stores for parts so I wouldn't get hit with crazy taxes TT.

![](https://fabricate.hackclub-assets.com/9d1f5e6678087655185101785cbbe7506cf1821f8a5309c7427cc3c2e3de92da/image-png/image.png)

**Total time spent: 7h**

# November 10, 2026 (entry 2): Finished the carts
<!-- fabricate:entry 2553 -->

I finished picking out all the parts across a few different sites to keep the total cost low and make sure everything was actually in stock. I got the Pro Micro nRF52840 boards, 1N4148 diodes, header strips, slide switches, and M2 screws from Robu.in, the Gateron switches and blank XDA keycaps from Meckeys.com, the 3.7V 300mAh LiPo batteries from ElectronicsComp.com (i couldnt find one that fits it anywhere else), and the PCBs from JLCPCB.com.

![](https://fabricate.hackclub-assets.com/9758e0d8016f5dd87ae51a5d4b09698c0e1cc5cb01e44d211bdbe6af2e10c43f/image-png/image.png)
![](https://fabricate.hackclub-assets.com/0d9b938826a4c8695ec1b9efcea8b7b662834714eb3b379a67c0350ac7540f83/image-png/image.png)
![](https://fabricate.hackclub-assets.com/412c5f9ea1a8cebb847b3c3c29d919b243a01214cabb30b7f3ad51715a2c9ad2/image-png/image.png)
![](https://fabricate.hackclub-assets.com/0a3c52ba33a2d34fea18f091421061f4555e961f4555e961f23d27163067f25fe475a4244/image-png/image.png)

**Total time spent: 1h**

# November 10, 2026 (entry 3): Made Readme, coded firmware
<!-- fabricate:entry 2556 -->

I set up the KMK firmware (code.py and boot.py) for wireless Bluetooth split mode between the two MCU boards, (i forgot it all since the last time i learned to make a macropad TT). I also put together the GitHub repo and wrote the first version of the readme with the parts list and build info.

![](https://fabricate.hackclub-assets.com/46ac9bf0d376f020535da28e80761a08cd14d660258b4e93bf334cb21dd3a0d5/image-png/image.png)

**Total time spent: 2h**

# November 14, 2026: Placeholder entry for time spent in the github setup
<!-- fabricate:entry 2988 -->

I spent an hour fixing git login issues on Windows (well atleast i learned something), organizing the repo into clean folders (Kicad/, CAD/, firmware/, and images/)(i later realized that i could just paste in images and hance there is no images folder), and recovering my README and journal files from an older git commit after force pushing accidentally wiped them.

![](https://fabricate.hackclub-assets.com/74bfc5eaab5f2b27824c5ebf554b205994993dd8a3383fc1dc0c70cf1d4bd3eb/image-png/image.png)

**Total time spent: 1h**

# November 21, 2026: Added BOM.CSV, schematic, Assembly CAD, and polish in readme
<!-- fabricate:entry 3577 -->

Since Ergogen skips the schematic step and only generates the PCB, I manually drew the full schematic in KiCad (scrappy_pcb2.kicad_sch) with all 34 switches, 34 diodes, the Pro Micro headers, battery pins and power switch. I also made a BOM.csv file with the verified total cost (₹7,037.23), added an intro paragraph to README.md explaining why I built the board, and started putting the switches and keycaps into the Fusion 360 case assembly.

![](https://fabricate.hackclub-assets.com/485be4c18bc512ccab0759e0ca86b86ff226f0bb9f96753cbb7d1b3794bb3d79/image-png/image.png)

**Total time spent: 3h 30m**

# November 21, 2026 (entry 2): Im dumb TT
<!-- fabricate:entry 3590 -->

While putting the full keyboard assembly together in Fusion 360, I realized the keycap models I imported were super high-poly triangle meshes instead of normal solid bodies. Every time I tried converting or duplicating all 68 keycaps and switches across both halves, Fusion 360 froze and crashed my PC multiple times TT.

![](https://fabricate.hackclub-assets.com/3eb617a03b8ca0d83110f3aad4de6ba28367ccd3c95aae4b22121b2b9c2f6d77/image-png/image.png)

**Total time spent: 2h**

# November 21, 2026 (entry 3): Just made it a .stl file
<!-- fabricate:entry 3598 -->

Because converting the high-poly keycap meshes into solid STEP bodies made the file balloon to like 1.2 gigs and completely froze my pc, I just exported the full combined assembly as a 54 MB STL (Assembeled.stl) so I could still check that all the keycaps fit inside the case walls without hitting anything.

![](https://fabricate.hackclub-assets.com/cba378f21b1153d2d7dbcd9781a304bdb1c926ddbb88764f44a7a3cf89c6f041/image-png/image.png)

**Total time spent: 18m**

# November 25, 2026: Clarification on Assembeled CAD model
<!-- fabricate:entry 3874 -->

I double-checked all the CAD files in the repo and confirmed that the combined case and keycap assembly is saved with all the other files (since exporting the model into one STEP file hits 1.2 GB and exceeds GitHub's file limits i exported it as a .stl file). I also checked the switch plate fit one more time so everything is ready for review.

![](https://fabricate.hackclub-assets.com/f93e5be230439f3554994443cd491a3427423de46f77914a28977ea8d647c69d/image-png/image.png)
![](https://fabricate.hackclub-assets.com/d5a4ec6da69f8078f231b36c4c41270e0cf336f36900e299ce1096c5fbd185c3/image-png/image.png)
![](https://fabricate.hackclub-assets.com/a673d22a9434b03dac97d370400c614b08cab3309712996841642b515d97645d/image-png/image.png)

**Total time spent: 6m**

# November 26, 2026: So i detailed the readme, journal and updated the BOM
<!-- fabricate:entry 3934 -->

![](https://fabricate.hackclub-assets.com/a8e14fd124f132066cd5f9ff4e6da730283423798a00787394cec929dddc6aba/image-png/image.png)
![](https://fabricate.hackclub-assets.com/2dcaaca0b55e00cde409c2b42a85eeecb9141d7411c49bd037efe411d958405c/image-png/image.png)
Some prices increased since the last time i made the BOM, so i updated it along with updating the case for the to fit more smoothly and cleanly with the case, also updated the Readme and journal as asked for after the review

**Total time spent: 1h**
