from glob import glob
import os

ROOT_PATH = 'custom/genshin'
RAW_DATA_PATH = 'raw_data/Genshin4.1_ZH/中文 - Chinese'
OUPUT_LIST_PATH = 'filelists/esd.list'
AUDIO_EXTENSION = 'wav'
TEXT_EXTENSION = 'lab'
SEPARATOR = '|'
LANGUAGE = 'ZH'

character_names = [
    '芙宁娜',
    '胡桃'
]

raw_data_path = os.path.join(ROOT_PATH, RAW_DATA_PATH)
output_list_path = os.path.join(ROOT_PATH, OUPUT_LIST_PATH)
with open(output_list_path, 'w') as f:
    for cn in character_names:
        audio_paths = glob(os.path.join(raw_data_path, cn, '*.wav'))
        print(f'Found {len(audio_paths)} voices for charactor {cn}')
        for ap in audio_paths:
            tp = os.path.splitext(ap)[0] + '.' + TEXT_EXTENSION
            if os.path.exists(tp):
                with open(tp, 'r') as tf:
                    t = tf.read()
                line = SEPARATOR.join([ap, cn, LANGUAGE, t])
                f.write(line + '\n')
            else:
                print('Does not exist:', tp)