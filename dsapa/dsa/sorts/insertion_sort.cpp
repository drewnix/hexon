#include <iostream>
#include <vector>

using namespace std;

int backwards_insertion_sort(vector<int>& sortvec) {
    for (int i=0; i <= sortvec.size(); i++) {
        int next_val = 0;
        bool move_rest = false;

        for (int j=0; j <= i; j++) {
            if (move_rest == true) {
                // temporarily save off the value we are going to replace
                int tmp = sortvec[j];

                // replace
                sortvec[j] = next_val;

                next_val = tmp;
            } else if (sortvec[j] > sortvec[i]) {
                // save j to move over 1
                next_val = sortvec[j];

                // assign i to j
                sortvec[j] = sortvec[i];

                // signal all i-j values need to be moved
                move_rest = true;
            }
        }
    }

    return 0;
}

int insertion_sort(vector<int>& sortvec) {
    for (int i=0; i <= sortvec.size(); i++) {
        int j = i;

        while (j > 0 && (sortvec[j-1] > sortvec[j])) {
            int tmp = sortvec[j-1];
            sortvec[j-1] = sortvec[j];
            sortvec[j] = tmp;
            j = j-1;
        }
    }

    return 0;
}


int main() {
    vector<int> v;
    int val;

    // push values into vector
    while(cin >> val) {
        v.push_back(val);
    }

    // sort vector
    backwards_insertion_sort(v);

    // output vector back out to stdout
    for (int i=0; i < v.size(); i++) {
        cout << v[i] << endl;
    }

    return 0;
}