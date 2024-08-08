import io
from typing import Text
from PIL import Image, ImageDraw, ImageFont


def draw_boxes(image_source, x1,y1,x2,y2):

    """Draw a border around the image using the hints in the vector list."""
    pillow_img = Image.open(io.BytesIO(image_source))
    draw = ImageDraw.Draw(pillow_img)

    #draw.line(((x1,y1),(x2,y2)),fill='green',width=8)

    draw.polygon([
    x1, y1,
    x2, y1,
    x2, y2,
    x1, y2], None, 'red')

    pillow_img.show()    

"""     
    draw.polygon([
        x0, y0,
        x1, y1,
        x2, y2,
        x3, y3], None, 'yellow')
 """



def drawVertices(image_source, vertices, display_text=''):
    pillow_img = Image.open(io.BytesIO(image_source))

    draw = ImageDraw.Draw(pillow_img)

    for i in range(len(vertices) - 1):
        draw.line(((vertices[i].x,vertices[i].y),(vertices[i+1].x,vertices[i+1].y)),fill='green',width=8)

    draw.line(((vertices[len(vertices)-1].x,vertices[len(vertices)-1].y),(vertices[0].x,vertices[0].y)),fill='green',width=8)

    font = ImageFont.truetype('arial.ttf',16)
    draw.text((vertices[0].x + 10, vertices[0].y),font=font, text=display_text,fill=(255,255,255))

    pillow_img.show()
    


""" 
def get_document_bounds(document, response, feature,bounds):
    for i,page in enumerate(document.pages):
        for block in page.blocks:
            if feature==BLOCK:
                bounds.append(block.bounding_box)
            for paragraph in block.paragraphs:
                if feature==PARA:
                    bounds.append(paragraph.bounding_box)
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature == SYMBOL):
                            bounds.append(symbol.bounding_box)
                    if (feature == WORD):
                        bounds.append(word.bounding_box)
    return bounds
 """