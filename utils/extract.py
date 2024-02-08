import re

class extract:
    class json:
        @classmethod
        def extract(cls, text):
            if "\n" in text:
                text = text.replace("\n", "")
            
            pattern = r"'question': *'([^']+)', *'answer': *'([^']+)'"
            json_pairs = re.findall(pattern, text)

            parsed_json_dicts = []
            for pair in json_pairs:
                question, answer = pair
                parsed_json_format = {'question': question, 'answer': answer}
                parsed_json_dicts.append(parsed_json_format)

            return parsed_json_dicts