from typing import Optional, Any
from langchain.tools import BaseTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from ..config.llm_config import get_llm
import os
from pydantic import Field

class CustomWebsiteSearchTool(BaseTool):
    name: str = Field(default="internet_search")
    description: str = Field(default="Search the internet for websites and information")
    search: Any = Field(default_factory=lambda: GoogleSerperAPIWrapper(serper_api_key=os.environ["SERPER_API_KEY"]))
    llm: Any = Field(default_factory=get_llm)

    def _run(self, query: str) -> str:
        try:
            results = self.search.results(query)
            return self._process_results(results)
        except Exception as e:
            return f"Error performing search: {str(e)}"

    def _process_results(self, results: dict) -> str:
        processed = []
        if 'organic' in results:
            for result in results['organic'][:5]:
                title = result.get('title', 'No title')
                link = result.get('link', 'No link')
                snippet = result.get('snippet', 'No description')
                processed.append(f"Title: {title}\nURL: {link}\nDescription: {snippet}\n")
        return "\n".join(processed) if processed else "No results found." 