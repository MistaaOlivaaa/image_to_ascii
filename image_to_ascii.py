from PIL import Image
import sys

def image_to_ascii(image_path, width=80, height=None):
    
    ascii_chars = "@%#*+=-:. "
    
    try:
        image = Image.open(image_path)
        image = image.convert('L')
        
        if height is None:
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio * 0.55)  
        
        
        image = image.resize((width, height))
        
        ascii_art = ""
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                ascii_index = int(pixel * (len(ascii_chars) - 1) / 255)
                ascii_art += ascii_chars[ascii_index]
            
            ascii_art += "\n"
        
        return ascii_art
        
    except FileNotFoundError:
        return f"Error: Image file '{image_path}' not found."
    except Exception as e:
        return f"Error processing image: {str(e)}"


def save_ascii_to_file(ascii_art, output_path):
    
    try:
        with open(output_path, 'w') as f:
            f.write(ascii_art)
        print(f"ASCII art saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {str(e)}")




if __name__ == "__main__":
    image_path = "example.jpg"  
    output_width = 80  
    output_height = None  
    
    print("Converting image to ASCII art...")
    print(f"Image: {image_path}")
    print(f"Output width: {output_width} characters")
    print("-" * 50)
    
   
    ascii_result = image_to_ascii(image_path, output_width, output_height)
    
    
    print(ascii_result)
    
   
    save_to_file = input("\nSave ASCII art to file? (y/n): ").lower().strip()
    if save_to_file == 'y':
        output_filename = input("Enter output filename (e.g., ascii_art.txt): ").strip()
        if output_filename:
            save_ascii_to_file(ascii_result, output_filename)
    
    print("\nDone!")