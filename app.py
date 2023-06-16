import os
import openai
from flask import Flask, render_template, jsonify, request

openai.organization = "org-PT3jCJ0gKRsqpqA07hgkcTBa"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
# openai.Model.list()
app = Flask(__name__)


def get_completion(prompt):
    print(prompt)
    query = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = query.choices[0].text
    print(response)
    return response


@app.route('/', methods=['GET', 'POST'])
def query_view():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = get_completion(prompt)
        return jsonify({'response': response})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
