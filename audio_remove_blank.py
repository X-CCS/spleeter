# from pydub import AudioSegment
# from pydub.utils import db_to_float
# from functools import reduce

# # Let's load up the audio we need...
# # podcast = AudioSegment.from_mp3("podcast.mp3")
# podcast = AudioSegment.from_wav("/Users/ccs/Desktop/fd1f4f0f01bba042579ee1a7de4679e7/vocals.wav")
# # intro = AudioSegment.from_wav("intro.wav")
# # outro = AudioSegment.from_wav("outro.wav")

# # Let's consider anything that is 30 decibels quieter than
# # the average volume of the podcast to be silence
# average_loudness = podcast.rms
# silence_threshold = average_loudness * db_to_float(-30)

# # filter out the silence
# podcast_parts = (ms for ms in podcast if ms.rms > silence_threshold)
# # combine all the chunks back together
# podcast = reduce(lambda a, b: a + b, podcast_parts)

# # add on the bumpers
# # podcast = intro + podcast + outro
# # save the result
# podcast.export("podcast_processed.wav", format="wav")
# print("done")

# from aukit import audio_normalizer
