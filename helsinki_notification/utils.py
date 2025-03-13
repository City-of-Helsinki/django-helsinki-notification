from helsinki_notification import constants


def map_translated_field(instance, field_name, langs=constants.LANGUAGES):
    return {lang: getattr(instance, f"{field_name}_{lang}") for lang in langs}
