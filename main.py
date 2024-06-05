from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_path, image_name, font_size=20):
    # Create a font object
    font = ImageFont.truetype(font_path, font_size)
    
    # Determine the size of the text to create an appropriately sized image
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Create a new image with a white background
    img = Image.new('RGB', (text_width + 20, text_height + 25), "white")
    draw = ImageDraw.Draw(img)
    
    # Draw the text onto the image
    draw.text((10, 10), text, fill="black", font=font)
    
    # Save the image
    img.save("output/" + image_name)

def text_file_to_images(file_path, font_path=None, font_size=20, extension='png'):
    with open(file_path, 'r', encoding='utf8') as file:
        for line_number, line in enumerate(file):
            text = line.strip()
            if text:
                image_name = f"output_line_{line_number + 1}.{extension}"
                text_to_image(text, font_path, image_name, font_size)
                print(f"Saved image for line {line_number + 1} as {image_name}")

text_file_to_images("example.txt", font_path="fonts/THSarabun Bold.ttf", font_size=40, extension='jpg')
