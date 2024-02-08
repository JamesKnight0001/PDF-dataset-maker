import json
from utils.pdf import PDF
from utils.instruct import agent
from utils.convert import Converter
from utils.extract import extract
from colorama import Fore, init
from config import pdf_location, dataset_name, section_skip, pdf_dataset_maker
import time

init()

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE

def pdf():
    data = PDF.get_data(fileloc=pdf_location)

    processed_pages = set()
    print(f"{green}### {white}Titles {green}###{white}")
    for i, page_info in enumerate(data):
        title = page_info['heading']
        print(f"{green}-{white} {title}")
    print(f"{green}### {white}Others {green}###{white}")
        
    for i, page_info in enumerate(data):
        if i in processed_pages:
            continue
        
        title = page_info['heading']

        if title in section_skip:
            print(f"{red}Skipping section: {title}{white}")
            processed_pages.add(i)
            continue
        
        print(f"{green}Processing section: {title}{white}")
        text = page_info['text']

        if len(text) > 1024:
            chunks = Converter.split_text(text)
            print(f"{green}Chunk count: {white}", len(chunks))
            for chunk in chunks:
                response = agent.summarize(title=title, text=chunk)
                if response is None:
                    print(f"{red}None{white}")
                else:
                    data = extract.json.extract(text=response)
                    for info in data:
                        question = info['question']
                        answer = info['answer']
                        Converter.add_jsonl(file_path=f"./{dataset_name}.jsonl", question=question, answer=answer)
                time.sleep(10)
        elif len(text) < 512:
            print(f"{red}Skipped {title}, due to low information.{white}")
            pass
        else:
            response = agent.summarize(title=title, text=text)
            if response is not None:
                data = extract.json.extract(text=response)
                for info in data:
                    question = info['question']
                    answer = info['answer']
                    Converter.add_jsonl(file_path=f"./{dataset_name}.jsonl", question=question, answer=answer)

        processed_pages.add(i)

if pdf_dataset_maker:
    pdf()
