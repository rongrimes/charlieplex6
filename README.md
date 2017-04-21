# charlieplex6

The experiment was to see how quickly I could charlieplex 2 x 3-led bar displays and drive it with a Raspberry Pi (2). Breadboarding was fairly simple - figuring it out on Fritzing took longer!

## The Board - Operational

![ezgif.com-1.gif](https://github.com/rongrimes/charlieplex6/blob/master/images/ezgif.com-1.gif)
  
## The Board - All

![Charlieplex6-9907.jpg](https://github.com/rongrimes/charlieplex6/blob/master/images/Charlieplex6-9907.jpg)  
The Raspberry Pi is mounted on the "official" touchscreen (which is not being used here) and is running from a 20Ah LiPo pack.

## Components
* Raspberry Pi (model not important)
* 2 x MU04 Light bars
  * MU04-2101 Red
  * MU04-4101 Yellow-Green
* 3 x 220 ohm resistors

The MU04 units are now obsolete and there's not even a Fritzing image for any of them. I replaced the LED bar with 3 discrete LEDs in the Breadboard image.

&nbsp;  

## Fritzing - Breadboard

![charlieplexing6-3_bb.png](https://github.com/rongrimes/charlieplex6/blob/master/images/charlieplexing6-3_bb.png)

## Fritzing - Schematic

![charlieplexing6-3_schem.png](https://github.com/rongrimes/charlieplex6/blob/master/images/charlieplexing6-3_schem.png)

Original diagram inspiration:
* [Wikipedia: Charlieplexing](https://en.wikipedia.org/wiki/Charlieplexing)
* [Circuit](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/3-pin_Charlieplexing_with_common_resistors.svg/330px-3-pin_Charlieplexing_with_common_resistors.svg.png)

&nbsp;  

## Code

Original code inspiration: [Github: raspberrypi_cookbook_ed2/charlieplexing.py](https://github.com/simonmonk/raspberrypi_cookbook_ed2/blob/master/charlieplexing.py) by Simon Monk  

Development from SM's code:
  * Constants used in the _pin_led_states_ table. This makes it more clear that the pins are tri-state with values: HI, LO, and INput mode.
  * Converted to Python3
  * Wrapup code added to respond gracefully to Ctl-C or a kill signal.
  * LED display closed down before program termination with the _clear_pins_ function

Ron  
April 20, 2017


