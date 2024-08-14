#from google.cloud import storage


from google.cloud import vision


def assemble_word(word):
    assembled_word=""
    for symbol in word.symbols:
        assembled_word+=symbol.text
    return assembled_word

def find_word_location(document,word_to_find):
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    if(assembled_word==word_to_find):
                        return word.bounding_box
                        #return word.bounding_box.bounding_poly.vertices
                    
    


def text_within(document,x1,y1,x2,y2):   

    text=""

    #breaks = vision.enums.TextAnnotation.DetectedBreak.BreakType
    #paragraphs = []
    #lines = []    

    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:                    
                for word in paragraph.words:
                    for symbol in word.symbols:
                        min_x = min(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
                        max_x = max(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
                        min_y = min(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
                        max_y = max(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)


                        
                        if(min_x >= x1 and max_x <= x2 and min_y >= y1 and max_y <= y2):
                                    text+=symbol.text
                        
    return text
