#include <algorithm>
#include <string>
#include <utility>
#include <vector>
#include <iterator>

using namespace std;

typedef struct Suffix {
  int index;
  pair<int, int> rank;
  Suffix(const int &i = -1): index(i), rank(-1, -1) {}
} Suffix;

inline bool operator <(const Suffix &s, const Suffix &other)
{
    return s.rank < other.rank;
}

vector<int> suffixArray(const string &s)
{
    int n = static_cast<int>(size(s));
    vector<Suffix> suffixes(size(s));
    vector<int> ranks(size(s));

    for (int i = 0; i < n; ++i) {
        suffixes[i].index = i;
        ranks[i] = s[i];
    }

    int length = 1;
    int limit = 2 * n;
    while (length < limit) {
        auto h = length / 2;        
        for (int i = 0; i < n; ++i) {
            auto &sf = suffixes[i];
            sf.rank.first = ranks[sf.index];
            sf.rank.second = sf.index + h < n ? ranks[sf.index+h] : -1;
        }
        sort(begin(suffixes), end(suffixes));

        auto rank = 0;
        ranks[suffixes[0].index] = rank;
        for (int i = 1; i < n; ++i) {
            auto &previous = suffixes[i-1];
            auto &current = suffixes[i];
            if (previous.rank != current.rank)
                ++rank;
            ranks[current.index] = rank;
        }
        length *= 2;
    }

    vector<int> indexes(n);
    transform(begin(suffixes), end(suffixes), begin(indexes), [](const Suffix &sf) -> int {
      return sf.index;
    });

    return indexes;
}

vector<int> lcpArray(const string &s, const vector<int> &suffixes)
{
    int n = static_cast<int>(size(s));
    int k = 0;
    vector<int> lengths(n, 0);
    vector<int> ranks(n, 0);

    for (int i = 0; i < n; ++i)
        ranks[suffixes[i]] = i;

    for (int i = 0; i < n; ++i) {
        if (ranks[i] == n - 1) {
            k = 0;
            continue;
        }

        int j = suffixes[ranks[i]+1];
        while (i + k < n && j + k < n && s[i+k] == s[j+k])
            ++k;

        lengths[ranks[i]] = k;
        k = max(k - 1, 0);
    }

    return lengths;
}
