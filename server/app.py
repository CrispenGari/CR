
from app import app
from flask import make_response, jsonify
from blueprints import blueprint

app.register_blueprint(blueprint, url_prefix="/api")
class AppConfig:
    PORT = 3001
    DEBUG = False
    
@app.route('/', methods=["GET"])
def meta():
    meta = {
        "programmer": "@crispengari",
        "main": "Character Recognition (CR)",
        "description": "given an image with text, CR API should be able to detect written text on the image in real time.",
        "language": "python",
        "libraries": ["easyorc", "PIL"],
    }
    return make_response(jsonify(meta)), 200

if __name__ == "__main__":
    app.run(debug=AppConfig().DEBUG, port=AppConfig().PORT, )