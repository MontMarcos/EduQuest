#include <bits/stdc++.h>
using namespace std;

int main(){
	int num = 0; 
	char rlt;
	for(int i = 0; i < 6; i++){
		cin >> rlt;
		if(rlt == 'V') {
			num++;
		}
	}

	if (num >= 5) {
    		cout << 1 << endl;
	}else if (num >= 3) {
    		cout << 2 << endl;
	}else if (num >= 1) {
    		cout << 3 << endl;
	}else if (num == 0) {
    		cout << -1 << endl;
	}

}

