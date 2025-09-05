#include <bits/stdc++.h>
using namespace std;

int main(){
	int esq; int dir;
	cin >>esq; 
	cin >>dir;

	int resul = (esq > dir) ? (esq+dir): 2*(dir-esq);

	cout << resul <<endl;
}
