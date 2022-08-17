// [main.cpp] C++ Source

// CHOMOLUNGM Programming Environment
// Compiler Tool  (Development 0.0.0.1)

// Main file

#include <iostream>
#include <string>

#include "compiler/arguments.hpp"
#include "compiler/exitoptions.hpp"
#include "compiler/main.hpp"

using namespace std;

int main( int argc, char** argv ) { 
    Argument arg = control( argc, argv );
    if(change( arg )) {
        mainWorking( arg.state );
    }
    return 0;
}
