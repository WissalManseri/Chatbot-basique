import random

# Définir les questions et réponses possibles
questions = {
    "Quel est ton nom ?": "Je suis un chatbot !",
    "Comment vas-tu ?": "Je vais bien, merci !",
    "Quelle est ta couleur préférée ?": "Je n'ai pas de préférence de couleur, je suis un programme !",
    "Quelle est la signification de la vie ?": "C'est une grande question, mais malheureusement je ne suis pas équipé pour y répondre..."
}

# Fonction pour répondre à une question donnée
def answer_question(question):
    # Vérifier si la question est dans les questions possibles
    if question in questions:
        return questions[question]
    # Sinon, donner une réponse aléatoire
    else:
        return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre question ?"

# Boucle principale pour recevoir des questions de l'utilisateur
while True:
    user_input = input("Vous: ")
    bot_response = answer_question(user_input)
    print("Chatbot:", bot_response)
