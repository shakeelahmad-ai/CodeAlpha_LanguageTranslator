from deep_translator import GoogleTranslator


class Translator:

    @staticmethod
    def translate(text, source_lang, target_lang):
        try:
            result = GoogleTranslator(
                source=source_lang,
                target=target_lang
            ).translate(text)

            return result

        except Exception as e:
            return f"Translation Error: {e}"