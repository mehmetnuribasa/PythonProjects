import re
import logging

class PaymentStructure:
    def __init__(self, payment_dict):
        self.payment_dict = payment_dict

    def get_payment(self, pages):
        """Retrieve the payment for the given number of pages."""
        for range_str, payment in self.payment_dict.items():
            if '-' in range_str:
                start, end = map(int, range_str.split('-'))
                if start <= pages <= end:
                    return payment
            elif int(range_str) == pages:
                return payment
        return self.payment_dict.get("default", 0)

class ArticleManager:
    def __init__(self, article_text, options):
        if not isinstance(article_text, str):
            raise ValueError("Article text must be a string.")
        
        self.article_text = article_text
        self.words_per_line = options.get('words_per_line', 12)
        self.lines_per_page = options.get('lines_per_page', 20)
        self.payment_structure = PaymentStructure(options.get('payment_structure', {}))
        self.pages = []
        self.paid_pages = 0
        self.words = []

        logging.basicConfig(level=logging.DEBUG)

    def split_into_pages(self):
        """Splits the article into pages with the given number of words per line and lines per page."""
        self.words = re.split(r'\s+', self.article_text.strip())

        lines = []
        for i in range(0, len(self.words), self.words_per_line):
            lines.append(' '.join(self.words[i:i + self.words_per_line]))

        self.pages = []
        for i in range(0, len(lines), self.lines_per_page):
            self.pages.append('\n'.join(lines[i:i + self.lines_per_page]))

        logging.debug(f"Total words: {len(self.words)}")
        logging.debug(f"Total lines: {len(lines)}")
        logging.debug(f"Total pages: {len(self.pages)}")

    def calculate_payment(self):
        """Calculates the payment based on the number of paid pages."""
        total_words = len(self.words)
        self.paid_pages = total_words // (self.words_per_line * self.lines_per_page)
        if total_words % (self.words_per_line * self.lines_per_page) != 0:
            self.paid_pages += 1  # Add one more page for partial pages

        logging.debug(f"Paid pages: {self.paid_pages}")
        return self.payment_structure.get_payment(self.paid_pages)

    def display_pages(self):
        """Displays all pages and the payment information."""
        payment = self.calculate_payment()
        print(f"Total Pages: {len(self.pages)}")
        print(f"Paid Pages: {self.paid_pages}")
        print(f"Payment Due: ${payment}")

        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")

    def process_article(self):
        """Handles the entire process of splitting the article and calculating payment."""
        self.split_into_pages()
        self.display_pages()

# Example usage
article_text = " ".join(["word"] * 240)  # 240 words to make one full page

options = {
    'words_per_line': 12,
    'lines_per_page': 20,
    'payment_structure': {
        "1": 30,
        "2": 30,
        "3-4": 60,
        "default": 100
    }
}

article_manager = ArticleManager(article_text, options)
article_manager.process_article()
