from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        
        result['Student Number'] = request.form.get('StudentNumber')
        
        result['University'] = request.form.get('University')

        result['Gender'] = request.form.get('gender')

        result['Major'] = request.form.get('major')

        email_id = request.form.get('email_id')
        email_domain = request.form.get('email_domain')
        result['Email'] = f"{email_id}@{email_domain}"

        result['Programming Languages'] = ', '.join(request.form.getlist('programming_languages[]'))

        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)