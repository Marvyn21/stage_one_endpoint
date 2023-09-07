from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import datetime

app = Flask(__name__)
api = Api(app)

class InfoResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('slack_name', type=str, required=True)
        parser.add_argument('track', type=str, required=True)
        args = parser.parse_args()
        
        slack_name = args['slack_name']
        track = args['track']
        current_day = datetime.datetime.utcnow().strftime('%A')
        utc_time = (datetime.datetime.utcnow() - datetime.timedelta(minutes=2)).strftime('%Y-%m-%dT%H:%M:%SZ')
        
        github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
        github_repo_url = "https://github.com/username/repo"
        
        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }
        
        return jsonify(response_data)

api.add_resource(InfoResource, '/api')

if __name__ == '__main__':
    app.run(debug=True)
