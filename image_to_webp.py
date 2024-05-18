from PIL import Image
import os

def convert_image_to_webp(input_path, output_path, quality=75):
    """
    Converts an image to WebP format.
    :param input_path: Path to the image to convert
    :param output_path: Path where the converted image will be saved
    :param quality: Quality of the output image (1-100)
    """
    # Open the image
    image = Image.open(input_path)
    
    # Save in WebP format
    image.save(output_path, 'WEBP', quality=quality)

def main():
    # Directory of input images and the output directory
    input_directory = 'path/to/your/input/images'
    output_directory = 'path/to/your/output/images'

    # Process all images in the directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('png', 'jpeg', 'jpg')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.webp')
            convert_image_to_webp(input_path, output_path)
            print(f'Converted {filename} to WebP format.')

if __name__ == '__main__':
    main()
