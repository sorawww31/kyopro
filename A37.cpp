#include <iostream>
using namespace std;
int main(){
    int N, M, B;
    cin >> N >> M >> B;
    int A;
    long long A_sum = 0;
    for(int i=0; i<N; i++){
        cin >> A;
        A_sum = A_sum + A;
    }

    int C;
    long long C_sum = 0;
    for(int i=0; i<M; i++){
        cin >> C;
        C_sum = C_sum + C;
    }

    long long Ans;
    Ans = A_sum * M + B*M*N + C_sum*N;
    cout << Ans << endl;
    return 0;
}