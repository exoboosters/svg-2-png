import os
from cairosvg import svg2png

# Define the color to replace and the new color
old_color = "#FF0000"  # Example: red
new_color = "#00FF00"  # Example: green
prefix = "new_"    # Prefix to append to new filenames

# Target dimensions
width = 512
height = 512

# Get all SVG files in the current directory
svg_files = [f for f in os.listdir('.') if f.lower().endswith('.svg')]

for filename in svg_files:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the old color with the new color
        updated_content = content.replace(old_color, new_color)

        # Create new filename
        name, _ = os.path.splitext(filename)
        sanitized_name = name.lower().replace(" ", "_")
        new_filename = f"{prefix}{sanitized_name}.png"

        # Convert updated SVG content to PNG
        svg2png(bytestring=updated_content.encode('utf-8'),
                write_to=new_filename,
                output_width=width,
                output_height=height)

        print(f"Converted: {filename} → {new_filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
