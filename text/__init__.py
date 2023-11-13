from text.symbols import *

_symbol_to_id = {s: i for i, s in enumerate(symbols)}


def cleaned_text_to_sequence(cleaned_text, tones, language):
    """Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
    """
    phones = [_symbol_to_id[symbol] for symbol in cleaned_text]
    tone_start = language_tone_start_map[language]
    tones = [i + tone_start for i in tones]
    lang_id = language_id_map[language]
    lang_ids = [lang_id for i in phones]
    return phones, tones, lang_ids


def get_bert(norm_text, word2ph, language, device):
    from .chinese_bert import get_bert_feature as zh_bert
    # from .english_bert_mock import get_bert_feature as en_bert
    # from .japanese_bert import get_bert_feature as jp_bert

    lang_bert_func_map = {"ZH": zh_bert}
    bert = lang_bert_func_map[language](norm_text, word2ph, device)  # get bert features for each phoneme: (n_ft, n_phonemes)
    return bert


def check_bert_models():
    import json
    from pathlib import Path

    from config import config
    from .bert_utils import _check_bert

    if config.mirror.lower() == "openi":
        import openi

        kwargs = {"token": config.openi_token} if config.openi_token else {}
        openi.login(**kwargs)

    with open("./bert/bert_models.json", "r") as fp:
        models = json.load(fp)
        for k, v in models.items():
            local_path = Path("./bert").joinpath(k)
            _check_bert(v["repo_id"], v["files"], local_path)
