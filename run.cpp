#include <iostream>
#include <string>
#include <fstream>
#include <curl/curl.h>

using namespace std;

ifstream inputFile("input.txt");
ifstream outputFile("output_url.txt");
ifstream outputFile("output_title.txt");

int main() {
	string s;
	int n,temp,dem;
	cin >> n;
	for (int i=1; i<=n ; i++){
		cin >> s;
		dem = 0;
		temp = 0;
		while (dem < 6 && temp < s.size()){
			while (s[temp] != '/') temp++;
			temp++;
			dem++;
		}
		if (dem == 6) {
			cout << s.substr(0,temp);
		}
	}
	return 0;
}