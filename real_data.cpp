#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(){
    ofstream outFile;
    outFile.open("real_data.json");

    srand (time(NULL));

    const float c1X = 2.0;
    const float c1Y = 1.8;
    const float c2X = 12.0;
    const float c2Y = 57.2;
    const float c3X = 88.1;
    const float c3Y = 22.4;
    const float c4X = 48.8;
    const float c4Y = 59.1;
    const float c5X = 83.0;
    const float c5Y = 90.1;


    float deltaX = 0.0;
    float deltaY = 0.0;
    float pointX = 0.0;
    float pointY = 0.0;
    int clustNum = 0;

    for (int i = 0; i < 10000; i++){
        deltaX = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
        deltaY = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
        clustNum = rand() % 13;

        switch(clustNum){
            case 0:
                pointX = c1X + deltaX * 4.0;
                pointY = c1Y + deltaY * 4.0;
                break;
            case 1:
                pointX = c1X + deltaX * 8.0;
                pointY = c1Y + deltaY * 9.0;
                break;
            case 2:
                pointX = c1X + deltaX * 10.0;
                pointY = c1Y + deltaY * 13.0;
                break;
            case 3:
                pointX = c2X + deltaX * 10.0;
                pointY = c2Y + deltaY * 10.0;
                break;
            case 4:
                pointX = c2X + deltaX * 14.0;
                pointY = c2Y + deltaY * 13.0;
                break;
            case 5:
                pointX = c3X + deltaX * 4.0;
                pointY = c3Y + deltaY * 4.0;
                break;
            case 6:
                pointX = c3X + deltaX * 7.0;
                pointY = c3Y + deltaY * 7.0;
                break;
            case 7:
                pointX = c4X + deltaX * 4.8;
                pointY = c4Y + deltaY * 4.5;
                break;
            case 8:
                pointX = c4X + deltaX * 8.0;
                pointY = c4Y + deltaY * 7.5;
                break;
            case 9:
                pointX = c4X + deltaX * 12.2;
                pointY = c4Y + deltaY * 12.0;
                break;
            case 10:
                pointX = c4X + deltaX * 18.3;
                pointY = c4Y + deltaY * 18.0;
                break;
            case 11:
                pointX = c5X + deltaX * 6.0;
                pointY = c5Y + deltaY * 6.0;
                break;
            case 12:
                pointX = deltaX * 100.0;
                pointY = deltaY * 100.0;
                break;
            default:
                cerr << "Bad cluster number " << clustNum << endl;

        }

        //cout << "X=" << pointX << " Y=" << pointY << " in cluster " << clustNum << endl;
        outFile << "{\"X\" : " << pointX << ", \"Y\" : " << pointY << "}\n";
    }

    return 0;
}
