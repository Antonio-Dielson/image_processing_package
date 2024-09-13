from PIL import Image

def combine_images(image_path1, image_path2, output_path):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    combined_width = image1.width + image2.width
    combined_height = max(image1.height, image2.height)

    combined_image = Image.new('RGB', (combined_width, combined_height))

    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (image1.width, 0))

    combined_image.save(output_path)
    print(f"Imagem combinada salva em: {output_path}")
