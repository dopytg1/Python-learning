coordinates = {
    'border_x': 12,
    'border_y': 6,
    'house_x': -8,
    'house_y': 35
}

if coordinates['border_x'] > coordinates['house_x'] and coordinates['border_y'] > coordinates['house_y']:
    print("SW")
elif coordinates['border_x'] < coordinates['house_x'] and coordinates['border_y'] < coordinates['house_y']:
    print("NE")
elif coordinates['border_x'] < coordinates['house_x'] and coordinates['border_y'] > coordinates['house_y']:
    print("SE")
elif coordinates['border_x'] > coordinates['house_x'] and coordinates['border_y'] < coordinates['house_y']:
    print("NW")
elif coordinates['border_x'] == coordinates['house_x'] and coordinates['border_y'] == coordinates['house_y']:
    print("border")