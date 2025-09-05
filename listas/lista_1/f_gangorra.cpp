#include<bits/stdc++.h>

using namespace std;

int main(){
	int p1, c1, p2, c2; cin >> p1 >> c1 >> p2 >> c2 ;

	cout << ((p1*c1) == (p2*c2) ? 0 : ((p1*c1) < (p2*c2) ? 1 : -1)) << endl;
}
