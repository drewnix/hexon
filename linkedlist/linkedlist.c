#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *head;

void recurse(struct Node *node) {
    if (node == NULL) {
        printf("end of list\n");
    } else {
        printf("recurse, curr_data = %d\n", node->data);
        recurse(node->next);
    }
}


/*
Time Complexity: O(n)
Space Complexity: O(1}
*/
void traverse() {
    struct Node *curr;

    curr = head;

    while(1) {
        if (curr == NULL) {
            printf("[N]\n");
            break;
        }

        printf("[%d]->", curr->data);
        curr = curr->next;
    }

}

/*
Time Complexity: O(1)
Space Complexity: None
*/
void insert_beginning(int data_val) {
    struct Node *new_node;

    new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data_val;

    if (head == NULL) {
       head = new_node;

       head->next = NULL;
    } else {
       new_node->next = head;

       head = new_node;
    }
}

void insert_end(int data_val) {
    struct Node *new_node;
    struct Node *curr;
    curr = head;

    new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data_val;

    while (1) {
        if (curr->next == NULL) {
            break;
        } else {
            curr = curr->next;
        }
    }

    curr->next = new_node;
}

void insert_position(int data_val, int p) {
    int i = 0;
    struct Node *curr, *prev;
    curr = head;


    while (i < position) {
        i++;

        if (curr->next == NULL) {}

    }
}

int main() {
    insert_beginning(5);
    insert_beginning(10);
    insert_beginning(20);
    insert_beginning(15);
    insert_end(99);

    //recurse(head);
    traverse();

    return 1;
}