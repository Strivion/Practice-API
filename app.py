from flask import Flask, jsonify, request

app = Flask(__name__)


FEEDBACK = []  # store feedback messages in memory


@app.route('/about')
def about():
    # Returns developer information as JSON
    return jsonify(
        name="Aaron Stevens",
        goals=[
            "Finish Honours degree in Software Development",
            "Achieve conversational fluency in Japanese",
            "Publish fantasy novels",
            "Release MMO-lite game project"
        ],
        skills=[
            "C++", "C#",
            "Blender", "Unreal Engine", "Game Design",
            "Creative Writing", "Japanese (JLPT N3 level)"
        ],
        fun_fact="I have an exceptional spatial memory—can recall building layouts years later."
    )


@app.route('/projects')
def projects():
    # Returns projects that I hvae made (or fake ones) as JSON
    return jsonify(
        projects=[
            "Making a simple API",
            "Made a classic Text based CMD Line RPG",
            "Developing an application for world domination"
        ]
    )



@app.route('/feedback', methods=['POST'])
# Accetps a JSON object from the user end and returns it as feedback.
def feedback():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify(error="Field 'message' is required"), 400

    FEEDBACK.append(message)
    return jsonify(ok=True, message=message), 201


@app.errorhandler(404)
# If message is missing/empty, this returns an error.
def not_found(error):
    return jsonify(
    error="The resource you requested could not be found.",
    status=404
    ), 404



if __name__ == '__main__':
    app.run()

