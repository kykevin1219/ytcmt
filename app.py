from flask import Flask, request, jsonify
import requests
from my_settings import google_api_key

app = Flask(__name__)

@app.route("/comments", methods = ["POST"])
def comments():
    data = request.json
    video_id = data["video_id"]
    request_url = f"""https://www.googleapis.com/youtube/v3/commentThreads?key={google_api_key}&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=10"""
    comments_data = requests.get(request_url)
    jsonized_data = comments_data.json()
    result = []
    comments_list = {
        "items" : jsonized_data["items"]
    }
    return jsonify(comments_list), 200

