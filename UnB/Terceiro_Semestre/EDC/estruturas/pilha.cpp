#include <bits/stdc++.h>
#include <stack>

using namespace std;
typedef stack <int> si;

int main(){
	si s; si s1; 
	
	s.push(10);
	s.push(1);
	s1.push(-10);
	s1.push(-1);

	cout << s.top() << s1.top() << endl;
	s.swap(s1);
	cout << s.top() << s1.top() << endl;
}
