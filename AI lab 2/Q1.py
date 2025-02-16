def classify_volume(volume):
    if 1 <= volume <= 10:
        return "Extra Small"
    elif 11 <= volume <= 25:
        return "Small"
    elif 26 <= volume <= 75:
        return "Medium"
    elif 76 <= volume <= 100:
        return "Large"
    elif 101 <= volume <= 250:
        return "Extra Large"
    else:
        return "Extra-Extra Large"

height = float(input("Enter height (cm): "))
width = float(input("Enter width (cm): "))
depth = float(input("Enter depth (cm): "))

volume = height * width * depth

label = classify_volume(volume)

print(f"The volume of the cube is {volume:.2f} cm³, which is classified as: {label}")
