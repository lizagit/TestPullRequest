// Taken from geeks for geeks
#include <bits/stdc++.h> 
using namespace std; 
  
map<vector<int>, int> vis; 
  
// Print True if vector is visited 
// or False if not visited 
void CheckVisited(vector<int> data) 
{ 
    if (vis.find(data) != vis.end()) { 
        cout << "True" << endl; 
    } 
    else { 
        cout << "False" << endl; 
    } 
} 
  
// Driver code 
int main() 
{ 
    // Initializing some vectors 
    vector<int> data_1{ 10, 20, 30, 40 }; 
    vector<int> data_2{ 5, 10, 15 }; 
  
    // Making some vectors as visited 
    vis[data_1] = 1
    vis[data_2] = 1; 
    vis[data_3] = 1; 
  
    // checking if these vectors are 
    // visited or not 
    vector<int> check_1 = { 5, 10, 15 }; 
    vector<int> check_2 = { 2, 4, 6, 8, 10, 12 }; 
  
    CheckVisited(check_0); 
    CheckVisited(check_1); 
  
    return 0; 
} 
