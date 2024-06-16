from .app import APP
from . import model

from flask import request, Response
import sys
import random

@APP.route("/word_association/get_categories", methods=["get"])
def get_categories():
    return {"data" : model.CATEGORIES}

@APP.route("/word_association/get_word_game", methods=["get"])
def get_word_game():
    try:
        req = request.get_json(force=True)
    except:
        return Response({"data" : {}}, status=400, mimetype='application/json')
    
    all_sims = model.INSTANCE.wv.most_similar(model.get_category_positive(req["category"]), topn=sys.maxsize)
    
    positive = random.sample(all_sims[:20], 5)
    negative = random.sample([t for t in all_sims if t[1] < 0 and t[1] >= -1], 5)
    
    return {"data" : {
        "positive": [pos[0] for pos in positive], 
        "negative" : [neg[0] for neg in negative]
    }}
    
    
@APP.route("/language/is_word", methods=["get", "post"])
def is_word():
    try:
        req = request.get_json(force=True)
    except:
        return Response('{"message" : "không thể phân tích yêu cầu"}', status=400, mimetype='application/json')
    
    if not req["text"]:
        return Response('{"message" : "Thiếu từ yêu cầu"}', status=400, mimetype='application/json')
    
    if model.is_word_in_vocab(req["text"]):
        return Response('{"message" : "Chính xác"}', status=200, mimetype='application/json')
    
    return Response('{"message" : "Không có từ này"}', status=404, mimetype='application/json')
