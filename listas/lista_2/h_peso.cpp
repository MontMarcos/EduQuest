#include <bits/stdc++.h>
using namespace std;
typedef vector <int> vi;

int main(){
	int n; cin >> n;
	
	bool eai = 0;

	vi nums(n);
	for(int i = 0; i < n; i++){
		cin >> nums[i];
	
	}

	for(int i = 0; i < n; i++){
		if((nums[i+1] - nums[i] >8)) {
			eai = 1;
			break;
		}

	}

	(eai == false) ? (cout << "S" << endl) : (cout << "N" << endl);
}
