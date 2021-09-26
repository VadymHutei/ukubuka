from modules.ACP.Translations.view import ACPTranslationsView
from modules.Language.service import LanguageService


class TranslationsController:

    def listAction(self):
        view = ACPTranslationsView('modules/ACP/Translations/list.html')
        languageService = LanguageService.getInstance()

        view.addData({
            'translations': languageService.getTranslations(),
            'languages': languageService.getLanguages(),
        })

        return view.render()