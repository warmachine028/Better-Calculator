# CHANGELOG

    Updated on: 15th July 2021

## [V4.2.1]

### _15th July 2021_

- Minor Update: Restructure and reduction of code
- Added a new BooleanVar Class in auxiliary.py to handle global booleans
- Shifted return_on_hovering(), change_on_hovering(), aot() to auxiliary.py
- Changed all configure() to coonfig()
- Inverted all if-else in toggle functions
- SEE CHANGELOG [auxiliary.py](..data\versions\auxiliary%20V1.1.py)
- _COMPATIBLE WITH auxiliary VER: 1.1_

## [V4.2.0]

### _28th June 2021_

- Major Update: Addition of History Clear functionalities
- Added 3 Buttons in History Frame
  - CLEAR ALL -> deletes all contents of log.txt
  - CLEAR LAST 10 -> deletes last 10 lines of log.txt
  - CLEAR LAST DAY -> deletes records of last date
- Added message box prompts for confirmations before deleting
- Added message box showingfo to notify after successful deletion
- Fixed Frame Glitch:
  - History Frame overlaps Scientific Frame
- Renamed few variables according to PEP8 Naming Conventions
- Reduced code by modifying calculate_sc()
- SEE CHANGELOG [auxiliary.py](..data\versions\auxiliary%20V1.0.py)
- _COMPATIBLE WITH auxiliary VER: 1.0_

## [V4.1.2]

### _26th June 2021_

- Minor Update: Reduced Code and added Type Hinting
- Removed redundant color settings from every widget
  instead used theme() function to reduce code
- Added more list comprehensions to reduce
- Optimized imports for faster execution

- Known Bugs:
  - History Frames Overlap Scientific Frame
- SEE CHANGELOG [auxiliary.py](..data\versions\auxiliary%20V0.2.py)
- _COMPATIBLE WITH auxiliary VER: 0.2_

## [V4.1.1]

### _24th June 2021_

- Minor Update: Reduction & Restructuring of Code
- Fixed glitch: which let window reopen in centre
  when history button is pressed
- Shifted colors to class Colours in auxiliary.py
- Shifted bconfigure() and sc_bconfigure() to auxiliary.py
  as createbtn() and createscibtn()
- Removed TypeError from click()
- Reverted lambda functions to normal functions
- SEE CHANGELOG [auxiliary.py](..data\versions\auxiliary%20V0.1.py)
- _COMPATIBLE WITH auxiliary VER: 0.1_

## [V4.1.0]

### _22nd March 2021_

- Minor Update: Reduction & Restructuring of Code
- Created new helper file _auxiliary.py_
- Shifted 4 Functions into helper file
- Restructured functions in main.py
  - imports
  - functions
  - body
- Added 2 new functions:
  - bconfigure(button, text, ro, col) -> Configures Button properties & packs
  - sc_bconfigure(button, text, ro, col) -> Configures Scientific Button properties & packs
- Replaced all toggle variables to BooleanVars for easy function access (no globals)
- Replaced Trigonometry functions to lambda functions
- SEE CHANGELOG [auxiliary.py](..data\versions\auxiliary%20V0.0.py)
- _COMPATIBLE WITH auxiliary VER: 0.0_

## [V4.1]

### _9th March 2021_

- Major Update: CALCULATION HISTORY
- Added `H` button on the top left corner
- Added 3 functions:
  - history() -> to pack_forget() frames, adjust geometry() and pack() history frame
  - scroll() -> to integrate mouse wheel to the Labels in Label_frame
  - show() -> to initialize '5' labels of Label_frame
- Added new frame for showing history
- Added Error checking for NULL log files with : Not enough data
- Equal button `=` now flashes on pressing return key

## [V4.0.1]

### _25th February 2021_

- Experimental Update
- Added a new feature to store history
- History of calculations stored in 'data/history.txt'

## [V4.0]

### _28th January 2021_

- Added a new theme: Midnight City
- Read README to know how to change themes
- Added new attribute: radio_fg
- Added 2 functions:
  - modify() -> to handle icon and title
  - \_geometry() -> to open calculator at the center

## [V3.4]

### _27th January 2021_

- Fixed a glitch on screen foreground color
- Rename primary script to 'main.py'
- Created folder "data" -> shifted 1 file
  - Colour_Arrtibutes.json -> 'data\themes.json'
- Created folder "icon" -> shifted 2 files
  - Cal_ico.ico -> 'icon.ico'
  - Calculator.png -> 'icon.png'
- "img" -> "Images" with renaming contents

## [V3.3]

### _2nd January 2021_

- Fixed redundant outputs on console
- Fixed |INV| button activebackground
  colour when |INV| activated
- Known Bugs:
  - App does'nt change selectcolor after changing theme

## [V3.2]

### _1st January 2021_

- Removed Unnecessary Code in change_theme() function
- Fixed (e) exponential power error

## [V3.1]

### _31st December 2020_

- Shortened Code by using DRY methodology
- Removed unnecessary Special Colours
- Added individual screen colours in "Colour_attributes"
- Added a change() function to handle theme changes
- Fixed !frame4.!frame2 not showing hover colours
- Fixed App crashes and inturrupts in inputs randomly

## [V3.0]

### _30th December 2020_

- Shortened the backend code
- Created new 'Colour_Attributes.json' file for more
  flexibility in theme customization in future updates
- Fixed Multiplication Button
- Fixed redundant texts in terminal/console
- Known Bugs:
  - App stops taking input randomly

## [V2.2]

### _29th December 2020_

- Fixed Active-foreground color Glitch
- over the Theme Radio Toggle Switches in Light theme
- Changed Multiplication Button from 'x' to "×"
- Changed Clear Button from "<-" to "⇐"
- Known Bugs:
  - Multiplication function not working.
  - Console filling with redundant texts 'frame...'

## [V2.1]

### _28th December 2020_

- Optimised Code
- Fixed Radio Buttons

## [V2.0]

### _27th December 2020_

- Optimised backend
- Reduced Code
- Fixed bugs

## [V1.4]

### _26th December 2020_

- Added more functionalities
- Fixed (^) button
- Fixed (e) button
- Known Bugs:
  - Radio buttons initially not chosen (Theme button)

## [V1.3]

### _25th December 2020_

- Minor improvements
- Superimproved Button Attributes in themes
- Fixed Inverse Button
- Known Bugs:
  - Not Working (^) Button
  - Not Working (e) Button

## [V1.2]

### _24th December 2020_

- Improved UI
- Added Seperate colour codings
- Added Exclusive Always on top feature
  (press calculator icon to Activate)
  - Dark:
    - Blue when Active
    - White while Deactive
  - Light:
    - Red when Active
    - Black while Deactive
- Known Bugs:
  - Not working inverse Buttons
  - Not Working (^) Button
  - Not Working (e) Button

## [V1.1]

### _23rd December 2020_

- 23rd December 2020
- Added Function to the INVERSE (INV) key
- INVERSE Bit Buggy in terms of themes

## [V1.0]

### _22nd December 2020_

- Added scientific mode
- Removed hover over glitches from light theme
- Added scientific properties
- Reduced Lot of unnecessary code
- Added Comments in code

## [V0.2]

### _21st December 2020_

- Reduced code for equal-screen `(enterclick())` function

## [V0.1]

### _20th December 2020_

- Added hover over widget feature
- Added comments in the code
- Added exclusive Zero Division Error output
- Entry Widget Screen font made significantly smaller for better looks
- Reduced Lot of unnecessary code

## [V0.0]

### _19th December 2020_

- Starting with the basics
- Added 2 themes
- Known Bugs:
  - Radio Button does'nt show theme initially
