#include <iostream>
using namespace std;


int main()
{
	int s[8];
	for (int i = 0; i < 8; i++){
		cin >> s[i];
	}
	bool as = 1, ds = 1, mx = 1;
	for (int i = 0; i < 8; i++){
		if (s[i] != i + 1)
			as = 0;
	}
	int ds_cnt = 8;
	for (int i = 0; i < 8; i++){
		if (s[i] != ds_cnt)
			ds = 0;
		ds_cnt--;
	}
	if (as)
		cout << "ascending";
	else if (ds)
		cout << "descending";
	else
		cout << "mixed";
	return 0;
}

