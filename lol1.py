import streamlit as st

from collections import Counter 
from string import punctuation
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stop_words
html_temp = """
    <div style="background-color:black ;padding:10px">
    <h1 style="color:white;text-align:center;">SUMMARIZE</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

html_temp69 = """
    <div style="background-color:white ;padding:10px">
    <h3 style="color:black;text-align:center;">PLEASE HAVE A LOOK AT THE SIDEBAR TO MAKE THE BEST USE OF SUMMARIZE.</h3>
    </div>
    """
st.markdown(html_temp69, unsafe_allow_html=True)

#st.markdown('<b>PLEASE HAVE A LOOK AT THE SIDEBAR TO MAKE THE BEST USE OF ANALYZE. </b>', unsafe_allow_html=True)




st.sidebar.header("YOU NO LONGER HAVE TO READ THOSE COMPLICATED WORDS!")

st.sidebar.markdown('<b>ABOUT:</b>', unsafe_allow_html=True)
st.sidebar.markdown("Remember when you had your exams on the next day and you just have to finish reading the last few pages of a novel, but couldn't?")
st.sidebar.markdown("Say no more! Summarize is here to your rescue")
st.sidebar.markdown('<b>HOW DOES IT WORK?:</b>', unsafe_allow_html=True)  
st.sidebar.markdown("Just copy-paste the text you want to Summarize and hit SUMMARIZE and there you have a much short and lucid text to read!")
st.sidebar.markdown("I made this project by using simple concepts of NLP like translation which I was taught in my final year of Engineering ")
st.sidebar.markdown('<b>CREATED BY:</b>', unsafe_allow_html=True)
st.sidebar.markdown('Nimisha Bhide')
st.sidebar.markdown('Email : nbhide.nb@gmail.com')
st.sidebar.markdown('Linkedin : https://www.linkedin.com/in/nimisha-bhide-108b22190/')

 

#uploaded_file = st.file_uploader("Upload your input txt file", type="txt")




user_input = st.text_area("Enter text here")
text = user_input


def tokenizer(s):
    tokens = []
    for word in s.split(' '):
        tokens.append(word.strip().lower())
    return tokens

def sent_tokenizer(s):
    sents = []
    for sent in s.split('.'):
        sents.append(sent.strip())
    return sents
#tokens = tokenizer(text)
#sents = sent_tokenizer(text)
def count_words(tokens):
    word_counts = {}
    for token in tokens:
        if token not in stop_words and token not in punctuation:
            if token not in word_counts.keys():
                word_counts[token] = 1
            else:
                word_counts[token] += 1
    return word_counts

#word_counts = count_words(tokens)

def word_freq_distribution(word_counts):
    freq_dist = {}
    max_freq = max(word_counts.values())
    for word in word_counts.keys():  
        freq_dist[word] = (word_counts[word]/max_freq)
    return freq_dist

#freq_dist = word_freq_distribution(word_counts)

def score_sentences(sents, freq_dist, max_len=40):
    sent_scores = {}  
    for sent in sents:
        words = sent.split(' ')
        for word in words:
            if word.lower() in freq_dist.keys():
                if len(words) < max_len:
                    if sent not in sent_scores.keys():
                        sent_scores[sent] = freq_dist[word.lower()]
                    else:
                        sent_scores[sent] += freq_dist[word.lower()]
    return sent_scores

#sent_scores = score_sentences(sents, freq_dist)

def summarize(sent_scores, k):
    top_sents = Counter(sent_scores) 
    summary = ''
    scores = []
    
    top = top_sents.most_common(k)
    for t in top: 
        summary += t[0].strip()+'. '
        scores.append((t[1], t[0]))
    return summary[:-1], scores
#summary, summary_sent_scores = summarize(sent_scores, 3)
#st.write(summary)




def main():

    tokens = tokenizer(text)
    sents = sent_tokenizer(text)
    word_counts = count_words(tokens)
    freq_dist = word_freq_distribution(word_counts)
    sent_scores = score_sentences(sents, freq_dist)
    summary, summary_sent_scores = summarize(sent_scores, 3)
    st.write(summary)
    
if st.button('summarize'):
    main()