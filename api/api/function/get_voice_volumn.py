# import wave
# import numpy as np
# import matplotlib.pyplot as plt

# '''
# 参考サイト
# https://tips-memo.com/python-db
# '''

# def to_db(x, N):
#     pad = np.zeros(N//2)
#     pad_data = np.concatenate([pad, x, pad])
#     rms = np.array([np.sqrt((1/N) * (np.sum(pad_data[i:i+N]))**2)
#                     for i in range(len(x))])
#     return 20 * np.log10(rms)


# def smoothing(input, window):
#     output = []
#     for i in range(input.shape[0]):
#         if i < window:
#             output.append(np.mean(input[:i+window+1]))
#         elif i > input.shape[0] - 1 - window:
#             output.append(np.mean(input[i:]))
#         else:
#             output.append(np.mean(input[i-window:i+window+1]))
#     return np.array(output)


# def get_voice_volumn(path):

#     wave_file = wave.open(path, "rb")  # Open
#     x = wave_file.readframes(wave_file.getnframes())  # frameの読み込み
#     x = np.frombuffer(x, dtype="int16")  # numpy.arrayに変換

#     N = 1024
#     db = to_db(x, N)

#     # 音量を可視化するプログラム
#     sr = 44100
#     t = np.arange(0, db.shape[0]/sr, 1/sr)

#     smoothed_db = smoothing(db, 100)

#     # 音量がマイナスに到達しているものは、採点の対象外とする
#     db_score = smoothed_db[smoothed_db > 0]

#     return np.average(db_score)
