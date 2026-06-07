from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'})
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'})

        calculation = f"{num1} {operation} {num2} = {result}"
        history.append(calculation)

        return jsonify({
            'result': result,
            'history': history[-10:]
        })

    except ValueError:
        return jsonify({'error': 'Please enter valid numbers'})

if __name__ == '__main__':
    app.run(debug=True)