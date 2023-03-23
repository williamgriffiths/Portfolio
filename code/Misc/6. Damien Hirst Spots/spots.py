import random
from PIL import Image, ImageDraw

def generate_spots_artwork(rows, columns, output_filename):
    spot_colors = [
        (196, 2, 51), (239, 82, 159), (255, 200, 87), (0, 173, 239), (28, 172, 120),
        (0, 104, 55), (0, 31, 63), (175, 111, 9), (48, 63, 159), (206, 17, 38),
        (255,145,194), (255,118,37), (1,190,212), (47,225,229), (255,112,108),
        (150,108,187), (210,240,249)
    ]

    spot_diameter = 1600 // (columns * 2 + 1)
    spot_radius = spot_diameter // 2
    img_size = (1600, 1280 + spot_diameter // 2)

    image = Image.new('RGB', img_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    def get_color_exclude(exclude_colors, available_colors):
        remaining_colors = [color for color in available_colors if color not in exclude_colors]
        if not remaining_colors:
            remaining_colors = [color for color in spot_colors if color not in exclude_colors]
        color = random.choice(remaining_colors)
        return color, remaining_colors


    available_colors_columns = [spot_colors.copy() for _ in range(columns)]

    for row in range(rows):
        for col in range(columns):
            x = col * 2 * spot_diameter + spot_radius + spot_diameter
            y = row * 2 * spot_diameter + spot_radius + spot_diameter

            exclude_colors = []
            if col > 0:
                left_color = image.getpixel((x - 2 * spot_diameter, y))
                exclude_colors.append(left_color)
                if row > 0:
                    top_left_color = image.getpixel((x - 2 * spot_diameter, y - 2 * spot_diameter))
                    exclude_colors.append(top_left_color)
                if row < rows - 1:
                    bottom_left_color = image.getpixel((x - 2 * spot_diameter, y + 2 * spot_diameter))
                    exclude_colors.append(bottom_left_color)

            if row > 0:
                top_color = image.getpixel((x, y - 2 * spot_diameter))
                exclude_colors.append(top_color)

            available_colors_column = available_colors_columns[col].copy()
            color, available_colors_column = get_color_exclude(exclude_colors, available_colors_column) 
            draw.ellipse([x - spot_radius, y - spot_radius, x + spot_radius, y + spot_radius], fill=color)
            available_colors_columns[col] = available_colors_column


    image.save(output_filename)

if __name__ == '__main__':
    rows = 8
    columns = 10
    output_folder = r'C:\Users\wgrif\Desktop\Website\Code\Misc\6. Damien Hirst Spots'
    iterations = 10
    for i in range(iterations):
        output_path = f'{output_folder}\\spots_artwork_{i+1}.png'
        generate_spots_artwork(rows, columns, output_path)
        print(f"Created Spots {i+1}/{iterations}.")
