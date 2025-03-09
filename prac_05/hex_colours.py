"""
CP1404/CP5632 Practical
The HEX_COLORS dictionary 
"""

HEX_COLORS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

# Case-insensitive input handling
color_input = input("Enter color name (blank to quit): ").strip().lower()
while color_input:
    try:
        # Access color directly with EAFP approach
        print(f"{color_input.title()}: {HEX_COLORS[color_input]}")
    except KeyError:
        print("Invalid color name")
    color_input = input("Enter color name (blank to quit): ").strip().lower()