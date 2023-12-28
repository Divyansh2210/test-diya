from flask import Flask, request, jsonify
import llamaindex
import openai

app = Flask(__name__)

# Initialize llamaindex with the knowledge base
knowledge_base_path = "path/to/knowledge-base"  # Replace with actual path
index = llamaindex.Index(knowledge_base_path)


@app.route('/process-input', methods=['POST'])
def process_input():
    user_query = request.json['query']
    relevant_sections = search_knowledge_base(user_query)
    if len(relevant_sections) < RELEVANCE_THRESHOLD:
        answer = "The answer is not available in the current knowledge base."
    else:
        answer = generate_answer(relevant_sections)
    return jsonify({"answer": answer})


def search_knowledge_base(query):
    results = index.search(query)
    return results


def generate_answer(relevant_sections):
    response = openai.Completion.create(
        model="gpt-4-turbo",
        prompt=create_prompt(relevant_sections),
        max_tokens=150
    )
    return response.choices[0].text


def create_prompt(relevant_sections):
    prompt = "Answer the following question based on this information: \n"
    prompt += "\n".join(relevant_sections)
    return prompt
