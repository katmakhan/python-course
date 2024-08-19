from PIL import Image, ImageDraw, ImageFont
import helper_functions as help_functions

# Load the image
base_image = Image.open(f"{help_functions.getscriptdir()}/Outputs/day_RELIANCE.png").convert("RGBA")

# Create a transparent overlay for the watermark
watermark = Image.new("RGBA", base_image.size, (255, 255, 255, 0))

# Initialize ImageDraw object
draw = ImageDraw.Draw(watermark)

# Define the watermark text and font
text = "Btech Traders"
font = ImageFont.load_default()

# Use textbbox to get the bounding box of the text
bbox = draw.textbbox((0, 0), text, font=font)

# The bounding box returns a tuple (left, top, right, bottom)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Load the logo image
logo = Image.open(f"{help_functions.getscriptdir()}/btech_icon.png").convert("RGBA")

# Resize the logo if needed
logo_width, logo_height = logo.size
scale_factor = 0.1  # Scale down the logo to 10% of the image width
new_logo_width = int(base_image.size[0] * scale_factor)
new_logo_height = int(logo_height * (new_logo_width / logo_width))
logo = logo.resize((new_logo_width, new_logo_height))

# Set the position of the logo watermark (centered)
logo_position = ((base_image.size[0] - new_logo_width) // 2, (base_image.size[1] - new_logo_height) // 2)

# Top Right
# logo_position = (
#     base_image.size[0] - text_width - 10,  # 10 pixels from the right edge
#     10  # 10 pixels from the top edge
# )

# Add transparency to the logo
logo.putalpha(255)  # 50% transparency

# Paste the logo onto the watermark
watermark.paste(logo, logo_position, logo)

# Center
# Calculate the position of the text below the logo
text_position = (
    (base_image.size[0] - text_width) // 2,
    logo_position[1] + new_logo_height + 10  # 10 pixels below the logo
)

# # Top Right
# text_position = (
#     base_image.size[0] - text_width - 10,  # 10 pixels from the right edge
#     10  # 10 pixels from the top edge
# )

# # Bottom Right
# text_position = (
#     base_image.size[0] - text_width - 10,  # 10 pixels from the right edge
#     base_image.size[1] - text_height - 10  # 10 pixels from the bottom edge
# )

# Draw the text on the watermark image with transparency
draw.text(text_position, text, (255, 255, 255, 128), font=font)  # Semi-transparent white

# Combine the base image with the watermark
watermarked_image = Image.alpha_composite(base_image, watermark)

# Save the final image
watermarked_image.save(f"{help_functions.getscriptdir()}/Outputs/watermarked_image.png")

# Optionally, display the watermarked image
watermarked_image.show()
