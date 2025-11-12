// Calculation of Pi in C++ according to the Leibniz rule

#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;

double calcPi(int n) {
    double pi = 0;
	double numer = 4.0;
    for(int i = 0; i < n ; i++) {
		double denom = (2*i+1);
		double term = numer/denom;
		if (i%2 == 1) pi = pi - term;
		else pi = pi + term;
	}
	return pi;
}

int main() {
	int terms = 1000;

    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(20);

	chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
	double pi = calcPi(terms);
	int duration = chrono::duration_cast<chrono::milliseconds>(std::chrono::steady_clock::now() - begin).count();
	
	cout << "PI: " << pi << endl;
	cout << "Elapsed Time (C++): " << duration << "ms" << endl;
}