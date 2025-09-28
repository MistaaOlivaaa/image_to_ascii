# Image to ASCII Art Converter

A simple Python script that converts images into ASCII art using text characters. Transform any image into beautiful text-based art that can be displayed in terminals, text files, or anywhere monospace fonts are supported.

## Features

- Convert any image format (JPEG, PNG, GIF, etc.) to ASCII art
- Customizable output width and height
- Automatic aspect ratio preservation
- Interactive file saving option
- Error handling for missing files and processing issues
- Optimized character mapping for better visual representation

## Sample Output

The converter transforms images like this colorful eye:

![Sample Image](example.jpg)

Into ASCII art like this:

```
@@@@@@@@##########**********++++++======----::::....    
@@@@@@########****++++=====----:::.....              
@@@@######****+++===---:::.....                      
@@##****+++===---::....                               
#***++==---::...                                      
```

## Requirements

- Python 3.6 or higher
- Pillow (PIL) library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MistaaOlivaaa/image_to_ascii
cd image-to-ascii
```

2. Install required dependencies:
```bash
pip install Pillow
```

## Usage

### Basic Usage

1. Place your image file in the same directory as the script
2. Update the `image_path` variable in the script to match your image filename
3. Run the script:

```bash
python image_to_ascii.py
```

### Customization Options

You can modify these variables in the `__main__` section:

- `image_path`: Path to your input image file
- `output_width`: Width of the ASCII output in characters (default: 80)
- `output_height`: Height of the ASCII output (default: auto-calculated to preserve aspect ratio)

### Example Usage

```python

ascii_result = image_to_ascii("your_image.jpg")

# Convert with custom dimensions
ascii_result = image_to_ascii("your_image.jpg", width=120, height=40)

# Save to file
save_ascii_to_file(ascii_result, "output.txt")
```

## How It Works

1. **Image Loading**: Opens and loads the specified image file
2. **Grayscale Conversion**: Converts the image to grayscale for better ASCII mapping
3. **Resizing**: Resizes the image to the specified dimensions while maintaining aspect ratio
4. **Character Mapping**: Maps pixel brightness values to ASCII characters using the gradient: `@%#*+=-:. `
5. **ASCII Generation**: Builds the final ASCII art string row by row
6. **Output**: Displays the result and optionally saves to a text file

## ASCII Character Set

The script uses a carefully chosen set of characters ordered from darkest to lightest:

```
@%#*+=-:. 
```

- `@` represents the darkest pixels
- ` ` (space) represents the lightest pixels

## File Structure

```
image-to-ascii/
├── image_to_ascii.py    # Main script
├── example.jpg          # Sample image
├── test.txt            # Sample ASCII output
├── README.md           # This file
└── .gitignore          # Git ignore file
```

## Error Handling

The script includes robust error handling for:

- Missing or invalid image files
- Unsupported image formats
- File permission issues
- Memory limitations for very large images

## Tips for Best Results

1. **Choose the right width**: 80-120 characters usually work well for most displays
2. **High contrast images**: Work better for ASCII conversion
3. **Simple