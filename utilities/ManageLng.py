from locale import getdefaultlocale

from languages import Hungarian, English


class ManageLng:
    def __init__(self, lang=None):

        if lang:
            if lang == "Hungarian":
                self.language_file = Hungarian.Hungarian()
            else:
                self.language_file = English.English()
        else:
            if getdefaultlocale()[0] == "hu_HU":
                self.language_file = Hungarian.Hungarian()
            else:
                self.language_file = English.English()

    def get_tr_text(self, text_id):
        if hasattr(self.language_file, text_id):
            return getattr(self.language_file, text_id)
        else:
            return "None"
