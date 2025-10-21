#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N, A[100001];
    cin >> N;
    for(int i=1; i <= N; i++){
        cin >> A[i];
    }
    // A + l, A + r で、l , r-1の間をソート
    sort(A +1, A + N + 1);
    int Q;
    cin >> Q;
    for(int i = 1; i <= Q; i++){
        int X;
        cin >> X;
        int pos = lower_bound(A+1, A + N + 1 , X) - A ;
      
        cout << pos - 1<< '\n';
        
        
    }
}