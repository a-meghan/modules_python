def moodResponse(mood_prompt):
    if mood_prompt.lower() == "happy":
        return "I'm glad you're having a good day today!"
    elif mood_prompt.lower() == "sad":
        return "I hope you feel  better soon!"
    elif mood_prompt.lower() == "mad":
        return "Let's take some deep breaths together... in -1...2...3-, out -1...2...3- and repeat."
    else:  
      return "I'm not sure how to respond to that mood. Can you try again?"
