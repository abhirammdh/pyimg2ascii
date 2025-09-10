from image2ascii import convert_image_to_ascii

ascii_art = convert_image_to_ascii("sample.png", new_width=80)

print(ascii_art)

with open("output.txt", "w") as f:
    f.write(ascii_art)
