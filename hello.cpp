#include <iostream>
#include <cstring>
using namespace std;

void login() {
    char password[8];

    cout << "Enter password: ";
    cin >> password;

    if (strcmp(password, "admin123") == 0)
        cout << "Login successful\n";
    else
        cout << "Login failed\n";
}

int main() {
    login();
}
