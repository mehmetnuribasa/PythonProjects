import re
import logging
import math

class ArticleManager:
    def __init__(self, article_text, options=None):
        # Validate article text
        if not isinstance(article_text, str) or not article_text.strip():
            raise ValueError("Article text must be a non-empty string.")
        self.article_text = article_text.strip()
        self.pages = []
        self.words = []
        
        # Set default options and override with provided options
        default_options = {
            'words_per_line': 12,
            'lines_per_page': 20,
            'payment_structure': {
                1: 30,
                2: 30,
                3: 60,
                4: 60,
                'default': 100,
            },
            'chunk_size': 1000  
        }
        if options is None:
            options = {}
        self.options = {**default_options, **options}

        # Set up logging for debugging
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

    def split_into_pages(self):
        words_per_line = self.options['words_per_line']
        lines_per_page = self.options['lines_per_page']
        chunk_size = self.options['chunk_size']

        # Split article text into words using regex for any whitespace
        word_iter = re.finditer(r'\S+', self.article_text)
        chunk_words = []
        current_lines = []

        for match in word_iter:
            chunk_words.append(match.group())
            if len(chunk_words) >= chunk_size:
                self._process_chunk(chunk_words, current_lines, words_per_line, lines_per_page)
                chunk_words = []

        # Process remaining words
        if chunk_words:
            self._process_chunk(chunk_words, current_lines, words_per_line, lines_per_page)

        # Add remaining lines into last page
        if current_lines:
            self.pages.append('\n'.join(current_lines))
            logging.debug(f"Added final partial page with {len(current_lines)} lines")

    def _process_chunk(self, chunk_words, current_lines, words_per_line, lines_per_page):
        for i in range(0, len(chunk_words), words_per_line):
            line_words = chunk_words[i:i + words_per_line]
            current_lines.append(' '.join(line_words))

            if len(current_lines) >= lines_per_page:
                self.pages.append('\n'.join(current_lines[:lines_per_page]))
                current_lines = current_lines[lines_per_page:]
                logging.debug(f"Processed page with {lines_per_page} lines")

        # Update current_lines for any remaining lines
        self.current_lines = current_lines

    def calculate_payment(self):
        payment_structure = self.options['payment_structure']
        total_pages = len(self.pages)
        total_words = len(re.findall(r'\S+', self.article_text))

        # Minimum word count for getting paid
        min_word_count = self.options.get('min_word_count', 240)
        if total_words < min_word_count:
            logging.debug(f"Total words ({total_words}) less than minimum required ({min_word_count}). No payment.")
            return 0

        # Find payment for total number of pages
        payment = payment_structure.get(total_pages, payment_structure.get('default', 0))
        logging.debug(f"Total pages: {total_pages}, Calculated payment: ${payment}")
        return payment

    def display_pages(self):
        payment = self.calculate_payment()
        print(f"Total Pages: {len(self.pages)}")
        print(f"Payment Due: ${payment}")

        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")
            logging.debug(f"Displayed page {index + 1}")

    def save_processed_article(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for index, page in enumerate(self.pages):
                    file.write(f"Page {index + 1}:\n{page}\n\n")
            logging.info(f"Processed article saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving processed article: {e}")
            raise

    def process_article(self):
        self.split_into_pages()
        self.display_pages()


# Example usage
if __name__ == "__main__":
    article_text = """Your article text goes here."""

    options = {
        'words_per_line': 12,
        'lines_per_page': 20,
        'payment_structure': {
            1: 30,
            2: 30,
            3: 60,
            4: 60,
            'default': 100,
        },
        'chunk_size': 1000,  # 
        'min_word_count': 240  
    }

    try:
        article_manager = ArticleManager(article_text, options)
        article_manager.process_article()
        # Save processed article to a file
        article_manager.save_processed_article('finished_article.txt')
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")