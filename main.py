import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels=["A", "B", "C", "D", "E", "F", "G", "H", "I", ],
    parents=["", "A", "A", "C", "C", "E", "A", "A", "G", "A", ]
))
# fig.show()

from PIL import Image
from pytesseract import pytesseract


def image_to_pdf(filename, output):
    images = []
    for file in filename:
        im = Image.open(file)
        im = im.convert("RGB")
        images.append(im)
        images[0].save(output, save_all=True, append_images=images[1:])


def extract_text_from_image(path):
    img = Image.open(path)
    tx = pytesseract.image_to_string(img)

    return tx


if __name__ == '__main__':
    # image_to_pdf(['data/image004.png'], 'output.pdf')
    print(extract_text_from_image("/Users/bolof/Documents/projects/fun-stuffs-with-python/data/kafka.png"))
