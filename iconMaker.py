import os
from PIL import Image

# Convert any png in this dir to ico file
def convert(image, icon):
    try:
        # Open the image
        img = Image.open(image)

        # Convert to RGBA mode (required for ICO format)
        img = img.convert("RGBA")

        # Resize the image to 256x256 (recommended for ICO format)
        img = img.resize((256, 256), Image.LANCZOS)

        # Save as ICO
        img.save(os.path.join(os.getcwd(), icon), format="ICO", sizes=[(256, 256)])

        print("Image converted to ICO successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


for file in os.listdir(os.getcwd()):
	if file.endswith('png'):
		png = os.path.join(os.getcwd(), file)
		ico = input("Icon File Name (with extension): ")
		convert(png, ico)
