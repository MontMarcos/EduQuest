#include <bits/stdc++.h>
using namespace std;

typedef vector<int>vi;

int main(){
	vi qtd(4);

	for(int i = 0; i <4;i++){
		cin >> qtd[i];
     	}

	for(int i = 0; i <3; i++ ){
		qtd[i] = qtd[i]-1;
	}

	cout << accumulate(qtd.begin(), qtd.end(), 0);
}
