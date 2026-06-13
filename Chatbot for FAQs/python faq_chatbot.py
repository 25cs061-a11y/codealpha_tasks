import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# FAQ Dataset (Questions and Answers)
faq_data = {
    "What is your return policy?":
        "You can return any product within 30 days of purchase.",

    "How can I track my order?":
        "You can track your order using the tracking link sent to your email.",

    "Do you offer international shipping?":
        "Yes, we offer international shipping to most countries.",

    "What payment methods do you accept?":
        "We accept Credit Cards, Debit Cards, UPI, Net Banking, and PayPal.",

    "How do I contact customer support?":
        "You can contact customer support at support@example.com.",

    "How long does delivery take?":
        "Delivery usually takes 3 to 7 business days.",

    "Can I cancel my order?":
        "Yes, you can cancel your order before it is shipped.",

    "Do you provide refunds?":
        "Yes, refunds are processed within 5 to 7 business days after approval.",

    "How can I reset my password?":
        "Click on the 'Forgot Password' option on the login page to reset your password.",

    "Is cash on delivery available?":
        "Yes, Cash on Delivery is available for selected locations."
}

questions = list(faq_data.keys())

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

# Preprocess all FAQ questions
processed_questions = [preprocess_text(q) for q in questions]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# Function to find the best matching FAQ answer
def get_answer(user_question):
    processed_input = preprocess_text(user_question)

    user_vector = vectorizer.transform([processed_input])

    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    # Similarity threshold
    if best_score < 0.20:
        return (
            "Sorry, I could not find a relevant answer for your question."
        )

    matched_question = questions[best_match_index]
    return faq_data[matched_question]

# Chatbot Interface
def chatbot():
    print("=" * 60)
    print("           FAQ CHATBOT USING NLP")
    print("=" * 60)
    print("Type 'exit' to quit the chatbot.")
    print()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Thank you for using the FAQ Chatbot. Goodbye!")
            break

        answer = get_answer(user_input)
        print("Bot:", answer)
        print()

# Main Program
if __name__ == "__main__":
    chatbot()