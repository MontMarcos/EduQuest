#include<bits/stdc++.h>
using namespace std;

int formula(int n){
	return ((n+1) * (n+2)/2);
}

int main(){
	int n; cin >> n;
	cout << formula(n) << endl;
}
