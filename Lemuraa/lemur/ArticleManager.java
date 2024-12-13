import java.util.*;

public class ArticleManager {
    private String articleText;
    private List<String> pages;
    private Map<String, Object> articleOptions;
    private List<String> words;
    private int paidPages;

    public ArticleManager(String articleText, Map<String, Object> articleOptions) {
        if (articleText == null || articleOptions == null) {
            throw new IllegalArgumentException("Article text and options must not be null.");
        }
        this.articleText = articleText;
        this.articleOptions = articleOptions;
        this.pages = new ArrayList<>();
        this.words = new ArrayList<>();
        this.paidPages = 0;
    }

    public void splitIntoPages() {
        int wordsPerLine = (int) articleOptions.get("wordsPerLine");
        int linesPerPage = (int) articleOptions.get("linesPerPage");

        words = Arrays.asList(articleText.trim().split("\\s+"));

        // Process lines
        List<String> lines = new ArrayList<>();
        for (int i = 0; i < words.size(); i += wordsPerLine) {
            int end = Math.min(i + wordsPerLine, words.size());
            lines.add(String.join(" ", words.subList(i, end)));
        }

        // Process pages
        for (int i = 0; i < lines.size(); i += linesPerPage) {
            int end = Math.min(i + linesPerPage, lines.size());
            pages.add(String.join("\n", lines.subList(i, end)));
        }
    }

    public int calculatePayment() {
        Map<String, Integer> paymentStructure = (Map<String, Integer>) articleOptions.get("paymentStructure");
        paidPages = (int) Math.ceil((double) words.size() / (20 * 12));
    
        System.out.println("Paid Pages: " + paidPages);  // Debugging line to check paidPages value.
    
        if (paidPages < 1) {
            return paymentStructure.get("default");
        }
    
        for (String range : paymentStructure.keySet()) {
            if (!range.equals("default")) {
                String[] limits = range.split("-");
                if (limits.length != 2) {
                    System.out.println("Invalid range format: " + range);  // Debugging invalid range.
                    continue;
                }
    
                int lower = Integer.parseInt(limits[0]);
                int upper = Integer.parseInt(limits[1]);
    
                System.out.println("Checking range: " + lower + " - " + upper);  // Debugging range check.
    
                if (paidPages >= lower && paidPages <= upper) {
                    return paymentStructure.get(range);
                }
            }
        }
    
        return paymentStructure.get("default");
    }
    

    public void displayPages() {
        int payment = calculatePayment();
        System.out.println("Total Pages: " + pages.size());
        System.out.println("Paid Pages: " + paidPages);
        System.out.println("Payment Due: $" + payment);

        for (int i = 0; i < pages.size(); i++) {
            System.out.println("\nPage " + (i + 1) + ":\n" + pages.get(i) + "\n");
        }
    }

    public void processArticle() {
        splitIntoPages();
        displayPages();
    }

    // Helper functions for configuration
    public static Map<String, Object> createArticleMap(int wordsPerLine, int linesPerPage, Map<String, Integer> paymentStructure) {
        Map<String, Object> articleOptions = new HashMap<>();
        articleOptions.put("wordsPerLine", wordsPerLine);
        articleOptions.put("linesPerPage", linesPerPage);
        articleOptions.put("paymentStructure", paymentStructure);
        return articleOptions;
    }

    public static Map<String, Integer> addPaymentStructure(Object... entries) {
        if (entries.length % 2 != 0) {
            throw new IllegalArgumentException("Invalid number of arguments; expected pairs of key and value.");
        }

        Map<String, Integer> paymentStructure = new HashMap<>();
        for (int i = 0; i < entries.length; i += 2) {
            paymentStructure.put((String) entries[i], (Integer) entries[i + 1]);
        }
        return paymentStructure;
    }

    // Main method for testing
    public static void main(String[] args) {
        String articleText = "Replace this with actual article content."; // Replace with your article
        Map<String, Integer> paymentStructure = addPaymentStructure("1-2", 30, "3-4", 60, "5-5", 100, "default", 0);
        Map<String, Object> articleOptions = createArticleMap(12, 20, paymentStructure);
    
        ArticleManager articleManager = new ArticleManager(articleText, articleOptions);
        articleManager.processArticle();
    }
    
}
