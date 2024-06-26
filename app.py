from flask import Flask, render_template, request

app = Flask(__name__)

def convert_base(num_str, from_base, to_base):
    """
    Convert a number string from one base to another.
    
    :param num_str: The number as a string in the source base.
    :param from_base: The base of the input number.
    :param to_base: The base to convert the number to.
    :return: The converted number as a string in the target base.
    """
    # Convert from the original base to decimal
    def to_decimal(num_str, from_base):
        return int(num_str, from_base)
    
    # Convert from decimal to the target base
    def from_decimal(num, to_base):
        if num == 0:
            return "0"
        digits = []
        while num:
            digits.append(int(num % to_base))
            num //= to_base
        digits = digits[::-1]
        # Convert digits to the appropriate base representation
        return ''.join(str(d) if d < 10 else chr(d - 10 + ord('A')) for d in digits)

    # Handle special cases for the bases
    if from_base < 2 or to_base < 2 or from_base > 36 or to_base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    # Convert from the original base to decimal
    decimal_num = to_decimal(num_str, from_base)
    
    # Convert from decimal to the target base
    return from_decimal(decimal_num, to_base)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_str = request.form['number']
        from_base = int(request.form['from_base'])
        to_base = int(request.form['to_base'])
        try:
            result = convert_base(num_str, from_base, to_base)
        except ValueError as e:
            result = str(e)
        return render_template('index.html', result=result, num_str=num_str, from_base=from_base, to_base=to_base)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
