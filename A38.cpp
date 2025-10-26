#include <iostream>
using namespace std;

long long D, N;
long long L[10001], R[10001], H[10001];
long long LIM[366];

int main(){
    cin >> D >> N;
    
    for(int i=1; i<=N; i++){
        cin >> L[i] >> R[i] >> H[i];
    }

    for(int i=1; i<=D; i++){
        LIM[i] = 24;
    }
    
    for(int i=1; i<= N; i++){
        for(int j = L[i]; j<=R[i]; j++){
            LIM[j] = min(LIM[j], H[i]);
        }
    }
    long long ans = 0;

    for(int i=1;i<=D;i++){
        ans = ans + LIM[i];
    }

    cout << ans <<  endl;

    return 0;
}