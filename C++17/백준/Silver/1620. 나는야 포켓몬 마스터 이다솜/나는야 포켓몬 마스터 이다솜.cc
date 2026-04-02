#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    int n, m;
    cin >> n >> m;

    map<string, int> m1;
    map<int, string> m2;

    for(int i = 1; i <= n; i++){
        string name;
        cin >> name;
        m1.insert({name, i});
        m2.insert({i, name});
    }

    for(int i = 0; i < m; i++){
        string question;
        cin >> question;

        if(question[0]>='0' && question[0]<='9'){
            int a=stoi(question);
            cout << m2[a] << "\n";  
        }
        else{
            cout << m1[question] << "\n";
        }   
    }
    return 0;
}
