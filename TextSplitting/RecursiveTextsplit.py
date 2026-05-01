from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """The RecursiveCharacterTextSplitter is a powerful tool for splitting text into smaller chunks while preserving the structure and meaning of the original text. It works by recursively splitting the text based on a specified separator, such as a newline character or a specific string. The splitter takes into account the context of the text and ensures that the resulting chunks are coherent and meaningful. This is particularly useful when dealing with large documents or when you want to process text in smaller segments for tasks such as natural language processing or machine learning.

 The RecursiveCharacterTextSplitter allows you to specify the chunk size and overlap, giving you control over how the text is split and ensuring that important information is not lost in the process. Overall, it is a valuable tool for anyone working with text data and looking to efficiently split it into manageable pieces while maintaining the integrity of the original content."""


spliter = RecursiveCharacterTextSplitter(
  chunk_size = 300,
  chunk_overlap = 0
)

chunks = spliter.split_text(text)
print(chunks)