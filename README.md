# Scrappy Keyboard

Wireless 68 key split mechanical keyboard running on ZMK firmware.

I majorly made this just for fun and to get back into making hardware, i used KiCad, fusion360 and Ergogen to wire the PCB, make the case and make the PCB respectively, also i made this because my current keyboard sucks TT

---

 **Layout:** 68 keys (total) with an ergonomic thumb cluster.
 
 **Firmware:** Wireless Bluetooth via ZMK firmware.
 
 **Microcontroller:** Dual Pro Micro nRF52840 boards with onboard LiPo charging circuitry.
 
 **Power:** 3.7V 300mAh KP-401230 Li-Po cells with hardware MSK12C02 slide cut-off switches.
 
 **Key Switches:** Gateron Milky Yellow Pro 5-pin linear switches clipped into a 1.5mm top plate.
 
---

## Design & Verification

### Schematic and PCB
* Reversable design
* Key matrix diodes
* B.Cu and F.cu GND copper plane

<img width="730" height="460" alt="image" src="https://github.com/user-attachments/assets/1196515a-bdaf-4ff4-bec0-f8460aa402ce" />

<img width="802" height="478" alt="image" src="https://github.com/user-attachments/assets/01a05198-72c6-4a04-ad8f-c4560a25016d" />

<img width="608" height="488" alt="image" src="https://github.com/user-attachments/assets/f15777e2-d4e6-448f-aaf5-2656a5390761" />

<img width="1214" height="672" alt="image" src="https://github.com/user-attachments/assets/a5069094-2d93-416c-9d66-b1e311616216" />

### Enclosure and Switch Plate
* Modeled in Fusion 360
* Precise cutouts for rear USB-C ports and side power switch actuators

<img width="1204" height="848" alt="image" src="https://github.com/user-attachments/assets/0fb802af-3925-4c50-811b-8c6bbc0d4fbc" />


---

## Bill of Materials (BOM)

(Exchange rate: ~₹92.63/USD - ~$82.01 USD total.)

| Sr.no | Name | Footprint | Amt | Source | Unit Price (INR) | Total (INR) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Pro Micro nRF52840 (Type-C / nice!nano v2 pinout) | 24-Pin ProMicro THT | 2 | [Robu.in](https://robu.in/product/promicro-nrf52840-development-board/) | ₹839.00 | ₹1,678.00 |
| 2 | 1N4148 Fast Switching Diodes | DO-35 Axial THT | 68 | [Robu.in](https://robu.in/product/1n4148-1w-zener-diode-pack-of-50/) | ₹1.24 | ₹84.32 |
| 3 | 2.54mm 1×40 Male Breakaway Header Strip | 2.54mm Pitch | 2 | [Robu.in](https://robu.in/product/2-54mm-1x40-pin-male-single-row-straight-short-header-strip-pack-of-3/) | ₹9.00 | ₹18.00 |
| 4 | MSK12C02-HB Horizontal SMD Slide Switch (SPDT) | SMD (C128955) | 2 | [Robu.in](https://robu.in/product/msk12c02-hb-shou-han-horizontal-attachment-50ma-single-pole-double-throw-spdt-12v-10000-times-black-smd-slide-switches-rohs/) | ₹8.00 | ₹16.00 |
| 5 | EasyMech SS 304 M2 × 10mm CSK Philips Screws (25 pcs) | M2 × 10mm | 1 pack | [Robu.in](https://robu.in/product/easymech-ss-304-csk-countersunk-philips-head-m2-x-10-mm-bolt-25-pcs/) | ₹123.00 | ₹123.00 |
| 6 | KP-401230 3.7V 300mAh LiPo Rechargeable Battery (4mm) *(Incl. 18% GST)* | 2-wire leads | 2 | [ElectronicsComp.com](https://www.electronicscomp.com/3.7v-300mah-lipo-battery-model-401230-india) | ₹171.10 | ₹342.20 |
| 7 | Gateron Milky Yellow Pro Linear Switches (5-Pin, 10-pack, 5% off 5+) | MX 5-Pin PCB Mount | 7 packs | [Meckeys.com](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-mechanical-pro-switch-5pin/?attribute_pa_switch-variation=pro-milky-yellow) | ₹189.05 | ₹1,323.35 |
| 8 | Blank XDA PBT Keycaps (1u, Set of 5, Black, 10% off 10+) | MX Stem | 14 sets | [Meckeys.com](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank/blank-xda-keycaps-1u/?attribute_pa_keycap-theme=black) | ₹125.10 | ₹1,751.40 |
| 9 | Custom Split Keyboard PCBs (159mm × 110mm, 2-layer) | Custom FR4 (5 pcs) | 1 order | [JLCPCB.com](https://jlcpcb.com/) | ₹1,148.61 | ₹1,148.61 |
| 10 | 3D Printed Case & 1.5mm Switch Plates | PLA / PETG (~120g) | 1 set | printing legion / self | ₹0.00 | ₹0.00 |
| 11 | Shipping & Courier Charges (JLCPCB $11.47 + ElectronicsComp ₹49) | Flat Rate | 1 | Various | ₹1,111.47 | ₹1,111.47 |
| **12** | **Total** | **Full Project Cost** | **—** | **—** | **—** | **₹7,596.35** |