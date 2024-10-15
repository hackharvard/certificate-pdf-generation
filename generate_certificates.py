import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Parameters (easily adjustable)
input_csv = 'players_per_row.csv'            # Path to the input CSV file
input_image_path = 'cert.png'                # Path to the input image
output_pdf_path = 'certificates.pdf'               # Path to the output PDF file
name_y_factor = 0.48                         # Adjusted position for the name
team_name_y_factor = 0.64                    # Adjusted position for the team name
font_path = 'Allura-Regular.ttf'             # Path to the font file for the hacker name
font_path2 = 'Montserrat-Bold.ttf'           # Path to the font file for the team name

# Define text colors
name_text_color = (200, 28, 62)              # Color #c81c3e in RGB
team_text_color = (0, 0, 0)                  # Black color for team name

# Read the CSV file
data = pd.read_csv(input_csv)

# capitalize the team names
data['Project Name'] = data['Project Name'].str.upper()

# capitalize the first letter of each word in the hacker names
data['Hacker Name'] = data['Hacker Name'].str.title()

# print how many rows are in the CSV file
print(f"Total rows in CSV: {len(data)}")

images = []

for index, row in data.iterrows():
    print(f"Processing row {index + 1}...")
    name = row['Hacker Name']
    team_name = row['Project Name']

    # Open the image
    img = Image.open(input_image_path).convert('RGB')
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Calculate initial font sizes as a fraction of image height
    name_font_size = int(height * 0.10)        # 10% of image height
    team_name_font_size = int(height * 0.10)   # 10% of image height

    # Maximum allowable text width (90% of image width)
    max_text_width = width * 0.8
    minimum_font_size = 10  # Minimum font size to prevent infinite loop

    # Load fonts
    try:
        name_font = ImageFont.truetype(font_path, name_font_size)
        team_name_font = ImageFont.truetype(font_path2, team_name_font_size)
    except IOError:
        print(f"Font file not found: {font_path} or {font_path2}")
        continue

    # Adjust name font size if necessary
    name_text_width = draw.textbbox((0, 0), name, font=name_font)[2]
    while name_text_width > max_text_width and name_font_size > minimum_font_size:
        name_font_size -= 1
        name_font = ImageFont.truetype(font_path, name_font_size)
        name_text_width = draw.textbbox((0, 0), name, font=name_font)[2]

    # Adjust team name font size if necessary
    team_text_width = draw.textbbox((0, 0), team_name, font=team_name_font)[2]
    while team_text_width > max_text_width and team_name_font_size > minimum_font_size:
        team_name_font_size -= 1
        team_name_font = ImageFont.truetype(font_path2, team_name_font_size)
        team_text_width = draw.textbbox((0, 0), team_name, font=team_name_font)[2]

    # Recalculate text sizes
    name_bbox = draw.textbbox((0, 0), name, font=name_font)
    name_text_width = name_bbox[2] - name_bbox[0]
    name_text_height = name_bbox[3] - name_bbox[1]

    team_bbox = draw.textbbox((0, 0), team_name, font=team_name_font)
    team_text_width = team_bbox[2] - team_bbox[0]
    team_text_height = team_bbox[3] - team_bbox[1]

    # Calculate positions
    name_x = (width - name_text_width) / 2
    name_y = height * name_y_factor - name_text_height / 2
    team_x = (width - team_text_width) / 2
    team_y = height * team_name_y_factor - team_text_height / 2

    # Draw text
    draw.text((name_x, name_y), name, fill=name_text_color, font=name_font)
    draw.text((team_x, team_y), team_name, fill=team_text_color, font=team_name_font)

    # Append the image to the list
    images.append(img)

# Save images to PDF
if images:
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF saved successfully at {output_pdf_path}")
else:
    print("No images to save.")
