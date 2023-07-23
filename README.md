# Pixelplace bot

A python pixelplace bot that is based on clicking on the screen and starts drawing the provided png image (pic.png) pixel by pixel. Supports most of the colors. (There is a scroll-back-to-top button therefore the last 5 colors are not implemented)

**Developers are not responsible for any damage caused by the app.**

# Setup

Note that since the script is based on clicking positions on the screen, the constant values absolutely have to be initialized and measured correctly. Also, the scroll-back-to-top button might be on a different position on different screens and cause problems for the colors. Finally, make sure that you did not scroll down in the color palette.  

Install the dependencies imported in the start of the program.  
Calculate the constant distances. (Use coord.py to get the current position of your mouse and calculate the required differences)  
**The required values include:**
- The distance between the center of two adjacent colors (from the color list)
- The distance between the center of two cells on the map
- The x, y position of the first color (white)
