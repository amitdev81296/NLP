from nltk.book import *
print("\n")

# A concordance view shows us every occurrence of a given word, together with some context
text1.concordance("monstrous")
print("\n")

# To examine words appearing in a similar range of contexts
text1.similar("monstrous")
print("\n")

# To examine just the contexts that are shared by two or more words
text2.common_contexts(["monstrous", "very"])