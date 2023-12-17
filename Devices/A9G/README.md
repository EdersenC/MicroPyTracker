
# A9G Development Board with MicroPython

## Introduction
This folder contains resources and information for setting up and using the A9G GPRS/GPS development board with MicroPython. The A9G is a versatile module suitable for integrating IoT capabilities into various projects.

## Setup and Documentation

### Official MicroPython Documentation for A9G
For a comprehensive guide on using the A9G module with MicroPython, refer to the official documentation available on GitHub:
- [MicroPython for A9G](https://github.com/pulkin/micropython/tree/master/ports/gprs_a9)

### External Setup Guide
A helpful external guide for getting started with the A9G development board can be found at:
- [Guide to AI-Thinker A9G GPRS/GPS Development Board](https://acoptex.com/wp/guide-to-ai-thinker-a9g-gprs-gps-development-board/)
- [Visual Guide to A9G MicroPython Flash](https://www.youtube.com/watch?v=8WAPMPTS3TQ&t=591s)

## Control Commands for A9G Board
When working with the A9G board in the MicroPython environment, the following control commands are useful:

- `CTRL-A`: On a blank line, enter raw REPL mode.
- `CTRL-B`: On a blank line, enter normal REPL mode.
- `CTRL-C`: Interrupt a running program.
- `CTRL-D`: On a blank line, do a soft reset of the board.
- `CTRL-E`: On a blank line, enter paste mode.

## Documentation

### Classes

#### FileHandler

- `init(self, folder,fileName, extension, fileType)`:
- `getFile(self):`: Returns The file location
- `getFolder(self):`: Returns the folder file's folder location
- `getFileName(self):`: Returns The file's name
- `read(self,mode = 'r+'):`: Returns the contents of the file as a string
- `remove(self):`: Removes The file 
- `cloneTo(self, folder ="",fileName = None, mode = "w", delete = False):`: Clones The file and its contents, to specified Location, with an Option to dlete old file(Hint: can use as moveTo).


  

