from flask import Flask
import random #підсключення бібліотеки рандом
app = Flask(__name__)

@app.route('/')
def random_n(): # створення функції для виведення випадкових чисел
    random_number=random.randint(1,6) #виведення випадкових чисел в діапазоні значень
    return f"Ваше випадкове число = {random_number}" 

