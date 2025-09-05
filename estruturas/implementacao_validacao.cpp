#include <bits/stdc++.h>
using namespace std;

bool valid(const string& expression){
	
	static map<char, char> open {{ ')' , '('}, {']' , '['}, {'}' , '{' }, };
	stack <char> s;

	for(auto c : expression){
		switch (c){
			case '(':
			case '{':
			case '[':
				s.push(c);
				break;
			case ')':
			case '}':
			case ']':
				if (s.empty() or s.top() != open[c]) return false;

			s.pop();
		}
	}
	return s.empty();
}

int main(){
	string str;
	getline(cin, str);
	cout << (valid(str) ? "OK" : "KO")<<endl;
}
