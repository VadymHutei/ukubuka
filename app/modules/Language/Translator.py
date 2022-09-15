from typing import Optional

from flask import g
from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.entities.TextEntity import TextEntity
from modules.Language.services.LanguageService import LanguageService


class Translator:

    _instance = None

    def __init__(self) -> None:
        self._language_service = LanguageService()

        self.default_language: LanguageEntity = self._language_service.get_default_language()
        self.languages: dict[str, LanguageEntity] = self._language_service.get_languages(only_active=True)
        self.available_languages: dict[str, LanguageEntity] = self._get_available_languages()
        self._texts: dict[int, TextEntity] = self._language_service.get_texts()
        self._text_IDs: dict[str, int] = self._get_text_IDs()

    def _get_available_languages(self) -> dict[str, LanguageEntity]:
        return {languageCode: language for languageCode, language in self.languages.items() if language.is_active}

    def _get_text_IDs(self) -> dict[str, int]:
        return {text_entity.text: text_entity.ID for text_entity in self._texts.values()}

    def _get_text_ID(self, text: str) -> Optional[int]:
        return self._text_IDs.get(text)

    def get_translation(self, text: str, language: str) -> Optional[str]:
        try:
            text_ID = self._get_text_ID(text)
            return self._texts[text_ID].translations[language]
        except:
            return None

    def _(self, text):
        return self.get_translation(text, g.current_language.code)

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = Translator()

        return cls._instance

    # def translate(self, text, language):
    #     if language is None:
    #         raise LanguageException(f'language must be not None')

    #     if language not in self.languages:
    #         raise LanguageException(f'The site does not support this language: {language}')

    #     textID = self._getTextIDByText(text)

    #     if (textID is None):
    #         textEntity = TextEntity({'text': text})
    #         self._language_service.addText(textEntity)
    #         self.setTexts()
    #         return text

    #     translation = self._texts[textID].translations.get(language)

    #     if translation is None:
    #         textTranslations = {}
    #         for languageCode in self.languages:
    #             textTranslations[languageCode] = ''
    #         self._texts[textID].translations = textTranslations
    #         self._language_service.updateTextTranslations(self._texts[textID])
    #         return text

    #     return translation if translation else text

    # def _(self, text, language=None):
    #     return self.translate(text, language or g.current_language.code)

    # def _setTranslations(self):
    #     translations = self._language_service.getTranslations()

    #     for textID in self._texts:
    #         if textID not in translations:
    #             textTranslations = {}
    #             for languageCode in self.languages:
    #                 textTranslations[languageCode] = ''
    #             self._texts[textID].translations = textTranslations
    #             self._language_service.updateTextTranslations(self._texts[textID])
    #         else:
    #             self._texts[textID].translations = translations[textID]

    # def _getTextIDByText(self, text):
    #     for textEntity in self._texts.values():
    #         if text == textEntity.text:
    #             return textEntity.ID
    #     return None
