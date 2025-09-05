#include <bits/stdc++.h>
using namespace std; 
typedef vector <int> vi;

int main(){
	int n, corte; cin >> n >> corte;
	vi notas(n);

	for(int i = 0; i < n; i++){
		cin >> notas[i];
	}

	sort(notas.begin(), notas.end(), greater<int>());

	cout << notas[corte-1] << endl;
}
