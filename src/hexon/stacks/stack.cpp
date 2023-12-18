#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class ArrayStack {
private:
    string* s;
    int N = 0;
    int slength = 16;
public:
    ArrayStack() {
        s = new string[slength];
    }

    string pop() {
        string word;

        if (N > 0) {
            word = s[--N];
            cout << "Pop: " << word << endl;

            // shrink array when size = 1/4th of total array size
            if (N < slength/4) {
                slength = slength/2;
                string* copy = new string[slength];
                for(int i=0; i <= N; i++)
                    copy[i] = s[i];

                // delete/free old array
                delete [] s;
                s = copy;
            }
        } else {
            cout << "Empty stack" << endl;
            word = "";
        }
        return  word;
    }

    void push(string word) {
        if (N > slength) {
            // allocate a new array
            slength = slength*2;
            string* copy = new string[slength];
            for(int i=0; i <= N; i++)
               copy[i] = s[i];

            delete [] s;
            s = copy;

        } else {
            s[N++] = word;
            cout << "N is: " << N << endl;
        }
    }
};

class Node {
public:
    Node(string new_word) { word = new_word; }
    string word;
    Node* prev;
};

class LinkedStack {
    Node* last = NULL;
public:
    string pop() {
        string word;

        if (last == NULL) {
            cout << "Empty stack" << endl;
            word = "";
        } else {
            word = last->word;
            last = last->prev;
            cout << "Pop: " << word << endl;
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
    //LinkedStack* stack = new LinkedStack;
    ArrayStack* stack = new ArrayStack();
    string word;

    while (cin >> word) {
        // words that are '-' pop the last item put on the stack
        if (word == "-") {
            stack->pop();
        } else {
            stack->push(word);
        }
    }

    return 0;
}
