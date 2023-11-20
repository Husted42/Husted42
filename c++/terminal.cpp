#include <iostream>
using namespace std;

// Define variables
string github = "C:\\C\\gitHub";
string colorScheme1 = "Campbell Powershell";

// Functions
// Defined as string but get's converted to const char* in main()
string runHPPS(string git) {
    string command =    "wt --colorScheme \"Tango Dark\" --startingDirectory " + git + "\\HPPS --title \"Github\" ; " 
                        "nt --colorScheme \"Tango Dark\" --startingDirectory " + git + "\\HPPS --title \"Main - Command Prompt\" ; "
                        "split-pane --colorScheme \"Ubuntu-ColorScheme\" -p \"Ubuntu\" --title \"Ubuntu\" ; "
                        "split-pane --colorScheme \"" + colorScheme1 + "\" --startingDirectory " + git + "\\HPPS -p \"Power Shell\" --title \"Sub - Power Shell\""
                        ;
    return command;
}

string runDefault(string git) {
    string command =    "wt --colorScheme \"Tango Dark\" --startingDirectory " + git + "\\HPPS --title \"Github\" ; "
                        "split-pane --colorScheme \"" + colorScheme1 + "\" --startingDirectory " + git + "\\HPPS --title \"Github\"";
    return command;
}

// Run program 
int main() {
    cout << "choose a profile: \n   (1) HPPS\n   (2) Default\n";
    int x;
    cin >> x;
    if (x == 1){
        string command = runHPPS(github);
        system(command.c_str());
    } else if (x==2) {
        string command = runDefault(github);
        system(command.c_str());
    } else {
        cout << " Not a vaild number " << endl;
    }
    _Exit(0);   
}