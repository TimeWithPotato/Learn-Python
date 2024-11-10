#include <iostream>
using namespace std;

// Function to compute the sum of multiples of k below n
long long sum_of_multiples(int k, int n) {
    int count = (n - 1) / k;  // Largest integer below n that is a multiple of k
    cout << k << " " << n << " " << count <<" "<<k*count*(count+1) / 2 << endl;
    return (long long) k * count * (count + 1) / 2;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        
        // Calculate the sum of multiples of 3, 5, and subtract multiples of 15
        long long sum = sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n);
        
        cout << sum << endl;
    }
    return 0;
}
