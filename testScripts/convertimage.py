import base64

# with open(r"C:\Users\Segun\Documents\IMG_20220805_153821_142.jpg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
#     print(encoded_string)
with open(r"C:\Users\Segun\Documents\IMG_20220621_163131_363.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(encoded_string)

print("      ")
print("completed")

# Optionally save to a file
with open(r"C:\Users\Segun\Documents\encoded_output2.txt", "w", encoding="utf-8") as f:
    f.write(encoded_string)
