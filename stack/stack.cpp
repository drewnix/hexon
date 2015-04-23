#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Node {
public:
    Node(string new_word) { word = new_word; }
    string word;
    Node* prev;
    Node* get_prev() { return prev; }
};

class Stack {
    Node* last = NULL;
public:
    string pop() {
        string word;

        if (last == NULL) {
            cout << "Error: empty stack!" << endl;
            word = "";
        } else {
            word = last->word;
            last = last->prev;
            cout << "Last word was: " << word << endl;
        }
        return word;
    }

    void push(string word) {
        Node* new_node = new Node(word);

        if (last == NULL) {
            new_node->prev = NULL;
            last = new_node;

        } else {
            new_node->prev = last;
            last = new_node;
        }
    }
};



int main() {
    string word;
    Stack* stack = new Stack;

    while (cin >> word) {
        if (word == "-") {
            stack->pop();
        } else {
            stack->push(word);
        }
    }

    return 0;
}
