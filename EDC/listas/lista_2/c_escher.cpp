#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;

int main(){
	int n; cin >> n;
	vi num(n); vi revNum(n);
	
	for(int i = 0; i < n; i++ ){
		cin >> num[i];
	}
	
	revNum = num;
	reverse(revNum.begin(), revNum.end());

	bool eai = 1;

	for(int i = 0; i < n; i++){
		if(num[i] + revNum[i] != num[0] + revNum[0]){
            		eai = false;
            		break;
        	}
	}
	
	if(eai == 0) cout << "N";
	else cout << "S";

}
