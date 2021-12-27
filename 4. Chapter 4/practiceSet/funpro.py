# Censor for the Bad Words

from better_profanity import profanity

# Input string
# text = "You piece of shit"
text = "You Motherfucker"

censored_text = profanity.censor(text)
print(censored_text)
