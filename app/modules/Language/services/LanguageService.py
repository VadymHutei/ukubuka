from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.entities.TextEntity import TextEntity
from modules.Language.repositories.LanguageRepository import LanguageRepository


class LanguageService:

    def __init__(self) -> None:
        self._language_repository = LanguageRepository()

    def get_default_language(self):
        return self._language_repository.get_default_language()

    def get_languages(self, only_active: bool = False) -> dict[str, LanguageEntity]:
        return self._language_repository.get_languages(only_active)

    def get_texts(self) -> dict[int, TextEntity]:
        return self._language_repository.get_texts()

    def getTexts(self):
        return {row['id']: TextEntity(row) for row in self._language_repository.getTexts()}

    def addText(self, textEntity):
        self._language_repository.addText(textEntity.text)
        if textEntity.translations:
            self.updateTextTranslations(textEntity)

    def _setTranslations(self):
        translations = self.getTranslations()
        for textEntity in self._texts:
            textEntity.translations = translations.get(textEntity.ID, {})

    def getTranslations(self):
        translations = {}

        for row in self._language_repository.getTranslations():
            if row['text_id'] not in translations:
                translations[row['text_id']] = {}
            translations[row['text_id']][row['language']] = row['translation']

        return translations

    def getTranslationsByTextID(self, textID):
        translations = self._language_repository.getTranslationsByTextID(textID)

        return {row['language']: row['translation'] for row in translations}

    def getTextByID(self, textID):
        textData = self._language_repository.getTextByID(textID)

        if textData is None:
            return None

        textEntity = TextEntity(textData)
        textEntity.translations = self.getTranslationsByTextID(textID)

        return textEntity

    def deleteTranslations(self, textID):
        self._language_repository.deleteTranslations(textID)

    def deleteText(self, textID):
        self._language_repository.deleteText(textID)

    def updateTextTranslations(self, textEntity):
        self._language_repository.updateTranslations({
            'textID': textEntity.ID,
            'translations': textEntity.translations,
        })
