#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
class Book{
    protected:
        string title;
        string author;
    public:
        Book(string t,string a){
            title=t;
            author=a;
        }
        virtual void display()=0;

};

class MyBook:public Book {
    public:
    int p;
    MyBook(string title, string author, int price):Book(title, author) {
        this -> p = price; // or we can assign the price to other variable
    }
    void display() {
        cout << "Title: " << title << endl << "Author: " << author << endl << "Price: " << p << endl;
    }
};
int main() {
    string title,author;
    int price;
    getline(cin,title);
    getline(cin,author);
    cin>>price;
    MyBook novel(title,author,price);
    novel.display();
    return 0;
}
