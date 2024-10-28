import mood_response
mood_prompt = input("How are you feeling today? ")
print(mood_response.moodResponse(mood_prompt))

import text_utils as tu
og_string = "This is my string to do things with"
print(f"This is my original string: {og_string}")

reversed_string = tu.reverse_a_string(og_string)
print(f"This is my reversed string: {reversed_string}")

caps_string = tu.capitalize_string(og_string)
print(f"This is my capitalized string: {caps_string}")