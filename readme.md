# PSX-Style Macro Pad

This is a very simple and hacking yet functional Macro-pad keyboard.
I am using a Pi Pico (RP2040) from WaveShare in the form of the RP2040-Zero.  

Since I only have 9 keys, and the RP2040 has more than enough GPIOs, I just wired each switch to a GPIO (0 through 8).  

Each GPIO is set as a pull-up input, and each switch bridges said GPIO to ground.
Just for some instinctive fear of peak currents, I also added a 1kOhm resister between all the switches and the ground-pin.
This is not strictly needed and may cause issues that I did not think of, but it works on my implementation.

## Finished Goods
![!FinishedCase](pics/done.jpg)
  
## Wiring
![!Wiring](pics/wiring.jpg)
