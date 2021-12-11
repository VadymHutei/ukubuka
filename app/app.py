from flask import Flask, request

from vendor.ukubuka.JinjaFilters import viewJinjaFilter

from modules.Language.services.LanguageService import LanguageService


app = Flask(__name__)

app.languageService = LanguageService()

app.jinja_env.filters['translate'] = app.languageService.translate
app.jinja_env.filters['pathWithLanguage'] = app.languageService.pathWithLanguage
app.jinja_env.filters['view'] = viewJinjaFilter

@app.before_request
def ctx():
    request.ctx = {}