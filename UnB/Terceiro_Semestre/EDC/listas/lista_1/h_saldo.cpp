#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;

int main(){
	int n, sld; 
	cin >> n >> sld; 
	vi valorA(n);
	int valores;

	for(int i = 0; i < n; i++){
		cin >> valores;
		(valorA[i] = sld+valores);
		sld = valores+sld;
	}
	
	sort(valorA.begin(), valorA.end());

	cout << *min(valorA.begin(), valorA.end());
}
