import os
from PIL import Image, ImageDraw, ImageFont

# Input text file path
input_file = 'fighting.txt'

# Set font and font size
font = ImageFont.truetype('../sjr.ttf', 24)

# Set output directory
output_dir = 'fighting'

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each line in the input file
with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        # Set output file name to be the same as the input line
        output_name = line.strip().replace(' ', '_')
        # Set output file path
        output_file = os.path.join(output_dir, output_name + '.png')

        # Create image
        image = Image.new('RGBA', (408, 600), color=(0, 0, 0, 0))

        # Draw text on image
        draw = ImageDraw.Draw(image)
        text_size = draw.textsize(line, font=font)
        x = 250 // 2
        y = 760 // 2
        draw.text((x, y), line, fill=(0, 0, 0), font=font)

        # Save image
        image.save(output_file)

        print(f"Image saved to {output_file}")
