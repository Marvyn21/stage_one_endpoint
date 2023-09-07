from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import datetime

app = Flask(__name__)
api = Api(app)

class InfoResource(Resource):
    def get(self):
        slack_name = request.args.get('slack_name')
        track = request.args.get('track')
        current_day = datetime.datetime.utcnow().strftime('%A')
        utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        
        github_file_url = "https://github.com/Marvyn21/stage_one_endpoint/blob/main/app.py"
        github_repo_url = "https://github.com/Marvyn21/stage_one_endpoint"
        
        return jsonify({
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        })
        
        return jsonify(response_data)

api.add_resource(InfoResource, '/api')

if __name__ == '__main__':
    app.run(debug=True)
