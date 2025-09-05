#include <bits/stdc++.h>
using namespace std;
typedef vector <int> vi;

int main(){
	vi idade(3);

	for(int i = 0; i < 3; i++){
		cin >> idade[i];
	}

	sort(idade.begin(), idade.end());
	
	cout << idade[1] << endl;
}
