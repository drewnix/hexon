#include <iostream>
#include <sstream>
#include <string>
#include <vector>


class QuickUnionUF {
 private:
    int *id;
    int id_len;

    // fetches the root id by following id[i] up
    int root(int i) {
        while(i != id[i]) i = id[i];
        return i;
    }
 public:
    QuickUnionUF(int N) {
        id = new int[N];
        id_len = N;
        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    bool connected(int p, int q) {
        return root(p) == root(q);
    }

    void s_union(int p, int q) {
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }

};

class QuickFindUF {
 private:
    int *id;
    int id_len;
 public:
    QuickFindUF(int N) {
        id = new int[N];
        id_len = N;
        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    // (O)n^2 implementation
    void s_union(int p, int q) {
        int pid = id[p];
        int qid = id[q];

        for (int i=0; i<id_len; i++) {
            if (id[i] == pid)
                id[i] = qid;
        }
    }

    bool connected(int p, int q) {
        return (id[p] == id[q]);
    }

    void show() {
        for (int i=0; i<id_len; i++) {
            printf("%d: %d\n", i, id[i]);
        }
    }
};

using namespace std;

template<typename T>
vector<T> split(const string& line) {
    istringstream is(line);
    return vector<T>(istream_iterator<T>(is), istream_iterator<T>());
}

int main() {
    int N;
    string line;

    cout << "Enter number of objects: ";
    cin >> N;

    QuickFindUF *qf = new QuickFindUF(N);

    getline(cin, line);

    while (getline(cin, line))
    {
        if (line.size() == 0)
            break;

        vector<int> vec = split<int>(line);
        int p, q;

        if (vec.size() < 2 || vec.size() > 2) {
            cout << "Error: must specify exactly two items.\n" << endl;

        } else {
            p = vec[0];
            q = vec[1];

            qf->s_union(p, q);
        }
    }

    qf->show();

    return 0;
}

