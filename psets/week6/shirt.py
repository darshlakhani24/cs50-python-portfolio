import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_extensions = (".jpg", ".jpeg", ".png")

    if not input_path.lower().endswith(valid_extensions) or not output_path.lower().endswith(valid_extensions):
        sys.exit("Input and output must be .jpg, .jpeg, or .png")

    if os.path.splitext(input_path)[1].lower() != os.path.splitext(output_path)[1].lower():
        sys.exit("Input and output must have the same extension")

    if not os.path.isfile(input_path):
        sys.exit(f"Input file does not exist: {input_path}")

    try:
        shirt = Image.open("shirt.png")
        input_img = Image.open(input_path)
        fitted = ImageOps.fit(input_img, shirt.size)
        fitted.paste(shirt, shirt)
        fitted.save(output_path)
    except Exception as e:
        sys.exit(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
