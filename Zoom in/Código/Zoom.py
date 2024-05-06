import cv2


def zoom_in(image_path, original_resolution):
    image = cv2.imread(image_path)
    zoomed_image = cv2.resize(image, original_resolution)
    return zoomed_image

def zoom_out(image_path, original_resolution):
    image = cv2.imread(image_path)
    zoomed_image = cv2.resize(image, original_resolution)
    return zoomed_image

relations = [
    ['Imagens/1.jpg', (150, 105), 'Zoom in', (704, 495)],
    ['Imagens/2.jpg', (200, 109), 'Zoom in', (654, 356)],
    ['Imagens/3.jpg', (140, 92), 'Zoom in', (1334, 880)],
    ['Imagens/4.jpg', (120, 76), 'Zoom in', (1033, 653)],
    ['Imagens/5.jpg', (300, 188), 'Zoom in', (909, 571)],
    ['Imagens/6.jpg', (1000, 750), 'Zoom out', (500, 375)],
    ['Imagens/7.jpg', (700, 933), 'Zoom out', (300, 400)],
    ['Imagens/8.jpg', (900, 675), 'Zoom out', (400, 300)],
    ['Imagens/9.jpg', (500, 668), 'Zoom out', (200, 267)],
    ['Imagens/10.jpg', (500, 376), 'Zoom out', (170, 128)]
]

for relation in relations:
    image_path, current_resolution, operation, original_resolution = relation
    if operation == 'Zoom in':
        zoomed_image = zoom_in(image_path, original_resolution)
    elif operation == 'Zoom out':
        zoomed_image = zoom_out(image_path, original_resolution)

    cv2.imshow(f'{operation} - {image_path}', zoomed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
