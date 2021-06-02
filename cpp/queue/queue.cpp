#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

/*
Things to add:
    - Generics (make a generic queue)
    - ArrayQueue implementation
*/

class Node {
public:
    Node(string new_word) { word = new_word; }
    string word;
    Node* next;
};

class LinkQueue {
    Node* head;
    Node* last;
public:
    LinkQueue() {
        last = NULL;
        head = NULL;
    }

    bool is_empty() {
        if (head == NULL) {
            return true;
        } else {
            return false;
        }
    }

    string dequeue() {
        string word;

        if (head != NULL) {
            word = head->word;
            head = head->next;

            cout << "Dequeue: " << word << endl;
        } else {
            cout << "Empty queue" << endl;
        }
        return word;
    }

    void enqueue(string word) {
        Node* temp = new Node(word);
        temp->next = NULL;

        if (last != NULL)
            last->next = temp;

        if (head == NULL)
            head = temp;

        last = temp;
    }
};

int main() {
    LinkQueue* queue = new LinkQueue();
    string word;

    while (cin >> word) {
        // words that are '-' dequeue the first item put in the queue
        if (word == "-") {
            queue->dequeue();
        } else {
            queue->enqueue(word);
        }
    }

    return 0;
}