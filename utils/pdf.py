from PyPDF2 import PdfReader

class PDF:
    @staticmethod
    def get_data(fileloc):
        data = []
        encountered = set()
        reader = PdfReader(fileloc)
        for page in reader.pages:
            heading, text = PDF.extract(page)
            if heading in encountered:
                for item in data:
                    if item["heading"] == heading:
                        item["text"] += "\n" + text
            else:
                data.append({"heading": heading, "text": text})
                encountered.add(heading)
        return data

    @staticmethod
    def extract(page):
        text = page.extract_text()
        lines = text.split('\n')
        heading = lines[0] if lines else ""
        text = '\n'.join(lines[1:])
        return heading, text