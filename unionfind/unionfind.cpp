#include <iostream>
#include <sstream>
#include <string>
#include <vector>

class QuickFindUF {
  private:
    int *id;
  public:
    QuickFindUF(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++)
            id[i] = i;

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

    QuickFindUF *qf = new QuickFindUF(10);

    cout << "Enter number of objects: ";
    cin >> N;

    while (getline(cin, line))
    {
        vector<int> vec = split<int>(line);
        int p, q;

        if (vec.size() < 2 || vec.size() > 2) {
            cout << "Error: must specify exacrtly two items.\n" << endl;

        } else {
            p = vec[0];
            q = vec[1];

            printf("p: %d, q: %d\n", p, q);
        }
    }

    return 0;
}

