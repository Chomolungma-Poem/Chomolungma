// [exitoptions.hpp] C++ Header

// CHOMOLUNGM Programming Environment
// Compiler Tool  (Dev 0.0.0.1)

// Exit Options Controller

#ifndef __CHOMOLUNGMA_COMPILER_EXITOPTIONS_HPP
#define __CHOMOLUNGMA_COMPILER_EXITOPTIONS_HPP

#include <string>
#include <iostream>

#include "compiler/arguments.hpp"

using namespace std;

const string USAGE = R"(
CHOMOLUNGMA Programming Environment
Compiler Tool

USAGE:
chomolungma compile [exit-options]
chomolungma compile [options] <filename>

Exit Options:
    -h, --help          Usage of the command
    -v, --version       Version of the tool
)";

const string VERSION = R"(
CHOMOLUNGMA Compiler [Development 0.0.0.1] 2022-08-17
)";

bool change( Argument arg ) {
    if( arg.stateNode == State::Help ) {
        cout << USAGE << endl;
        return false;
    }
    if( arg.stateNode == State::Version ) {
        cout << VERSION << endl;
        return false;
    }
    return true;
}

#endif
