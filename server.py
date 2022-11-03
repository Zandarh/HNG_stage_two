from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def post():
    # Unpacking the data posted to the API
    reqJson = request.get_json()
    operation_string = reqJson['operation_type']
    x = reqJson['x']
    y = reqJson['y']

    result = None
    the_operation = None

    # split the string part of the dictionary into a list for easy traversing
    operations = operation_string.split()
    for operation_type in operations:
        # checking for the operator to use
        if operation_type == "minus" or operation_type == "substract" or operation_type == "substraction":
            the_operation = operation_type
            result = x - y
        if operation_type == "add" or operation_type == "addition":
            the_operation = operation_type
            result = x + y
        if operation_type == "multiply" or operation_type == "multiplication":
            the_operation = operation_type
            result = x * y
    the_dict = {"slackUsername": "zandarh",
    "result": result,
    "operation_type": the_operation
    }
    return (the_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
