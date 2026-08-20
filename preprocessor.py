import json

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from llm_helper import llm


def extract_metadata(post):
    template = """
You are given an X post. You need to extract:
- Number of lines
- Language of the post
- Tags

Requirements:
1. Return only valid JSON.
2. No preamble or explanation.
3. JSON must contain exactly these keys:
   - line_count
   - language
   - tags
4. "tags" should be an array with at least two tags.

Post:
{post}
"""

    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    response = chain.invoke({"post": post})

    try:
        parser = JsonOutputParser()
        return parser.parse(response.content)
    except OutputParserException as e:
        raise OutputParserException(f"Failed to parse response: {e}")


def get_unified_tags(posts_with_metadata):
    unique_tags = set()

    for post in posts_with_metadata:
        unique_tags.update(post["tags"])

    unique_tags_list = ", ".join(unique_tags)

    template = """
I will give you a list of tags.

Requirements:
1. Merge similar tags.
   Example:
   "Ai" and "Artificial Intelligence" → "Ai"
   "Healthy" and "Health" → "Health"
   "Technology" and "Tech" → "Tech"

2. Use Title Case.

3. Return ONLY valid JSON.

Example:
{
    "Artificial Intelligence":"Ai",
    "Healthy":"Health",
    "Technology":"Tech"
}

Tags:
{unique_tags_list}
"""

    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    response = chain.invoke({"unique_tags_list": unique_tags_list})

    try:
        parser = JsonOutputParser()
        return parser.parse(response.content)
    except OutputParserException as e:
        raise OutputParserException(f"Failed to unify tags: {e}")


def process_posts(
    raw_file_path,
    processed_file_path="processed_post.json"
):
    try:
        with open(raw_file_path, "r", encoding="utf-8") as file:
            posts = json.load(file)

        enriched_posts = []

        for post in posts:
            metadata = extract_metadata(post["text"])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

        unified_tags = get_unified_tags(enriched_posts)

        for post in enriched_posts:
            current_tags = post["tags"]
            new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
            post["tags"] = list(new_tags)

        with open(processed_file_path, "w", encoding="utf-8") as file:
            json.dump(enriched_posts, file, indent=4)

        print("Processed posts saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    process_posts(
        "raw_post.json",
        "processed_post.json"
    )