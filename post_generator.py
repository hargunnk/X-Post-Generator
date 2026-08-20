import llm_helper

print("Imported llm_helper from:", llm_helper.__file__)


from llm_helper import llm
from prompt_based import PromptBasedLearning

prompt_based = PromptBasedLearning()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    elif length == "Long":
        return "11 to 15 lines"
    else:
        return "5 to 10 lines"


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f"""
Generate an X (Twitter) post using the information below.
Do not include any preamble.

1. Topic: {tag}
2. Length: {length_str}
3. Language: {language}

The generated post should always be in English.
"""

    examples = prompt_based.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "\n\nUse the writing style of the following examples:\n"

        for i, post in enumerate(examples):
            post_text = post["text"]
            prompt += f"\nExample {i+1}:\n{post_text}\n"

            # Use a maximum of 2 examples
            if i == 1:
                break

    return prompt