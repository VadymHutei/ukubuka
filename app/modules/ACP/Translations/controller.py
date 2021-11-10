from modules.ACP.Translations.views.ACPTranslationsView import ACPTranslationsView
from modules.ACP.Translations.views.ACPTranslationsEditView import ACPTranslationsEditView
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

    def editAction(self):
        view = ACPTranslationsEditView('modules/ACP/Translations/edit.html')

        return view.render()