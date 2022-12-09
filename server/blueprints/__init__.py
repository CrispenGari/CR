from flask import Blueprint, make_response, jsonify, request
import io
from PIL import Image
import easyocr as ocr
# allowed languages
languages = "abq ady af ang ar as ava az be bg bh bho bn bs ch_sim ch_tra che cs cy da dar de en es et fa fr ga gom hi hr hu id inh is it ja kbd kn ko ku la lbe lez lt lv mah mai mi mn mr ms mt ne new nl no oc pi pl pt ro ru rs_cyrillic rs_latin sck sk sl sq sv sw ta tab te tjk tl tr ug uk ur uz vi".split(' ')
# allowed images 
allowed_extensions = ['.jpg', '.JPG', '.png' ,'.PNG' ,'.jpeg' ,'.JPEG']

blueprint = Blueprint("blueprint", __name__)
@blueprint.route('/v1/recognize', methods=["POST"]) 
def detect_text():
    data = {"success": False}
    reader = ocr.Reader(["ch_sim", "en"], gpu=False)
    if request.method == "POST":
        if request.files.get("image"):
            img = request.files.get("image")
            ext = "."+str(img.filename).split('.')[-1]
            if not ext in allowed_extensions:
                data["success"] = False
                data['error'] = f'Only images with extensions ({", ".join(allowed_extensions)}) are allowed.'
                # read the image in PIL format
            else:
                try:
                    image = request.files.get("image").read()
                    image = Image.open(io.BytesIO(image))
                    data["success"] = True
                    results = reader.readtext(image, detail=0)
                    data['results'] = results
                except Exception as e:
                    print(e)
                    data["error"] =  "Something went wrong on the server."
                    data["success"] = False
                    
    else:
        data["error"] =  "Only POST method is allowed in this route."
        data["success"] = False
        return make_response(jsonify(data)), 400

    return make_response(jsonify(data)), 200
    
    