from flask import redirect
from http import HTTPStatus

def home():
    return redirect('https://gitlab.com/lourivanRluz/desafio-dev-jr-pl/-/blob/main/README.md'),HTTPStatus.SEE_OTHER