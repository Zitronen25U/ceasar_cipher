import ntlk

ntlk.download('words', quiet=True)
ntlk.download('names', quiet=True)

from ntlk.corpus import words, names

corpus_words = words.words()
corpus_names = names.words()