from modules.Language.Translator import Translator


def translate(text, language=None):
    translator = Translator.getInstance()
    return translator.translate(text, language)

def pathWithLanguage(path, language):
    pathSegments = path.split('/')

    if not pathSegments:
        return f'/{language}/'

    translator = Translator.getInstance()
    del pathSegments[0]
    
    if pathSegments[0] in translator.languages:
        pathSegments[0] = language
    else:
        pathSegments.insert(0, language)

    return '/' + '/'.join(pathSegments)

def view(x):
	if x is None:
		return ''
	if isinstance(x, bool):
		return 'yes' if x else 'no'
	return x