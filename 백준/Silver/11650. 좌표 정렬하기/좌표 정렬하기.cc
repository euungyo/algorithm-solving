#include <iostream>
#include <algorithm>

using namespace std;

struct point{
    int x;
    int y;
};

bool sorting(point p1, point p2){
    if(p1.x == p2.x){
        return p1.y < p2.y;
    }
    else{
        return p1.x < p2.x;
    }
}


int main(){
    int t; cin >>t;
    point points[100001];

    for(int i=0;i<t;i++){
        cin >> points[i].x >> points[i].y;
    }

    sort(points,points+t,sorting);

    for (int i=0;i<t;i++){
        cout << points[i].x << " " << points[i].y << "\n";
    }

    return 0;
}