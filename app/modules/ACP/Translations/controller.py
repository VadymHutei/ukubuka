from modules.ACP.Translations.view import ACPTranslationsView
from modules.Language.service import LanguageService


class TranslationsController:

    def listAction(self):
        view = ACPTranslationsView('modules/ACP/Translations/list.html')
        languageService = LanguageService.getInstance()

        view.addData({
            'texts': languageService.texts,
            'languages': languageService.languages,
        })

        return view.render()