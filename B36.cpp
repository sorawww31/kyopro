#include <iostream>
using namespace std;

int main(){
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;
    int cnt0=0, cnt1=0;

    // 0と1を数える
    for(int i=0;i<N;i++){
        if (S[i] == '0'){
            cnt0++;
        }
        else{
            cnt1++;
        }
    }

    if(abs(cnt1-K) % 2 == 0){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }

    return 0;
}