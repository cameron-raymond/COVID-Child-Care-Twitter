from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import unidecode
import nltk
import re


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

lemma = WordNetLemmatizer()
stopwords = stopwords.words('english')

def clean_text(text):
    text = text.lower()
    # Remove urls
    text = re.sub('http[s]?://\S+', '', text)

    text = unidecode.unidecode(text)
    text = re.sub("[+-/]", ' ', text)
    # remove emojis
    text = emoji_pattern.sub(r'', text)
    token_words = word_tokenize(text)
    pos_tags = nltk.pos_tag(token_words)
    stem_text=[]
    for token,pos in pos_tags:
        token = re.sub("[>@,\.!?'()…]", '', token)
        if token not in stopwords and len(token) > 3:
            pos_tag = get_wordnet_pos(pos)
            token = lemma.lemmatize(token,pos=pos_tag) if pos_tag else token
            stem_text.append(token)
    return ' '.join(stem_text)

       
if __name__ == "__main__":
    print(clean_text("He was running and eating in Québec at same time. He has bad habit of swimming after playing long hours in the Sun."))