import openai
from newspaper import Article

class ArticleSummarizer:

    def __init__(self, api_key:str): 
        openai.api_key = api_key
        self.api_key = api_key

    def get_aws_doc(self, news_url:str):
        article = Article(news_url)
        article.download()
        article.parse()
        return article

    def news_summarizer(self, content:str):
        system_prompt = """ Assume the role of an AWS technical writer skilled in simplifying complex information. Summarize the AWS documentation found at [URL] into a high-level, concise overview that highlights essential concepts, recommended steps, best practices, and potential use cases, specifically tailored for beginner to intermediate cloud computing users. Avoid technical jargon unless necessary, and explain any key terms in simple language. Organize the summary into sections if multiple topics are covered, and keep the response within 300 words. Ensure the summary communicates practical applications or value propositions of the AWS services discussed, making it accessible for readers with minimal AWS experience and providing actionable insights.

        """
        struct = [{"role": "system", "content": system_prompt}]
        struct.append({"role": "user", "content": content})
        chat = openai.chat.completions.create(model="gpt-4o-mini", messages = struct)
        response = chat.choices[0].message.content
        struct.append({"role": "assistant", "content": response})
        return response
        
    