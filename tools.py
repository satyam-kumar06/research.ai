from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    print(f"[DEBUG] save_to_txt called with data:\n{data}")

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(formatted_text)
        print(f"[DEBUG] Data successfully saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to write to file: {e}")


save_tool = Tool(
    name= "save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_characters_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
