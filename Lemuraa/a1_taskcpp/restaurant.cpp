#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MenuItem {
public:
    string name;
    double price;

    MenuItem(string name, double price) {
        this->name = name;
        this->price = price;
    }
};

class RestaurantMenu {
private:
    vector<MenuItem> menuItems;

public:
    void addItem(string name, double price) {
        menuItems.push_back(MenuItem(name, price));
    }

    void displayMenu() {
        cout << "=== Restoran Menüsü ===" << endl;
        for (int i = 0; i < menuItems.size(); i++) {
            cout << i + 1 << ". " << menuItems[i].name << " - " << menuItems[i].price << " TL" << endl;
        }
    }

    double getItemPrice(int index) {
        if (index >= 1 && index <= menuItems.size()) {
            return menuItems[index - 1].price;
        }
        return 0.0;
    }

    string getItemName(int index) {
        if (index >= 1 && index <= menuItems.size()) {
            return menuItems[index - 1].name;
        }
        return "";
    }
};

class Order {
private:
    vector<pair<MenuItem, int>> orderedItems;

public:
    void addOrder(MenuItem item, int quantity) {
        orderedItems.push_back({item, quantity});
    }

    void displayOrder() {
        double total = 0.0;
        cout << "\n=== Siparişleriniz ===" << endl;
        for (auto& order : orderedItems) {
            double itemTotal = order.first.price * order.second;
            cout << order.first.name << " x" << order.second << " = " << itemTotal << " TL" << endl;
            total += itemTotal;
        }
        cout << "\nToplam Tutar: " << total << " TL" << endl;
    }
};

int main() {
    RestaurantMenu menu;
    menu.addItem("Köfte", 50.0);
    menu.addItem("Pizza", 70.0);
    menu.addItem("Hamburger", 40.0);
    menu.addItem("Salata", 20.0);
    menu.addItem("Çorba", 15.0);

    Order order;
    int choice, quantity;

    while (true) {
        menu.displayMenu();

        cout << "\nSipariş vermek için menüden bir öğe numarası seçin (0 ile çıkış yapabilirsiniz): ";
        cin >> choice;

        if (choice == 0) {
            break;
        }

        cout << "Kaç adet sipariş etmek istersiniz? ";
        cin >> quantity;

        if (quantity <= 0) {
            cout << "Lütfen pozitif bir miktar girin." << endl;
            continue;
        }

        double itemPrice = menu.getItemPrice(choice);
        if (itemPrice > 0) {
            order.addOrder(MenuItem(menu.getItemName(choice), itemPrice), quantity);
        } else {
            cout << "Geçersiz seçim, tekrar deneyin." << endl;
        }
    }

    order.displayOrder();

    return 0;
}