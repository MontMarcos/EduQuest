#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;

int main(){
    vi num(100); 
    int f = 0, s = 0;

    for(int i = 0; i < 5; i++){
        cin >> num[i];
    }

    sort(num.begin(), num.begin() + 5, greater<int>());

    for(int i = 0; i < 5; i++){
        if(num[i] == num[0]) f++;
        else break;
    }

    for(int i = f; i < 5; i++){
        if(num[i] == num[f]) s++;
        else break;
    }

    cout << f << " " << s << endl;
}

