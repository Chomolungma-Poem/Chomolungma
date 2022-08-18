// [arguments.hpp] C++ Header

// CHOMOLUNGM Programming Environment
// Compiler Tool  (Dev 0.0.0.1)

// Arguments Controller

#ifndef __CHOMOLUNGMA_COMPILER_ARGUMENTS_HPP
#define __CHOMOLUNGMA_COMPILER_ARGUMENTS_HPP

#include <string>
#include <iostream>

#include "clipp.h"

using namespace std;
using namespace clipp;

struct Peg {
    const bool is = true;
};

struct StdState {
    string filename;
};

enum class State {
    Help,
    Version,
    State
};

struct Argument {
    parsing_result result;
    
    union {
        Peg help;
        Peg version;

        StdState state;
    };
    State stateNode;

    Argument(  ) {
        stateNode = State::State;
    }
    Argument( const State stat ) {
        stateNode = stat;
    }
    Argument( const Argument& arg ) {
        stateNode = arg.stateNode;
    }
    ~Argument(  ) {

    }
};

#if true
#define CHECKING_INIT \
    Argument* arg = new Argument(  ); \
    bool flag;
#endif

#if true
#define CHECK( message ) \
    flag = false; \
    arg->result = parse( argc, argv, message ); \
    if(flag == true)
#endif

#if true
#define CHECKING_FLAG( message ) \
    message.set( flag )
#endif

#if true
#define CHECK_OPTION( flag1, flag2 ) \
    CHECK( group( CHECKING_FLAG( option( flag1, flag2 ) ) ) )
#endif

Argument* control( int argc, char** argv ) {
    CHECKING_INIT
    CHECK_OPTION( "-h", "--help" ) {
        arg->stateNode = State::Help;
        return arg;
    }
    CHECK_OPTION( "-v", "--version" ) {
        arg->stateNode = State::Version;
        return arg;
    }
    CHECK( group(
    CHECKING_FLAG( value( "filename", arg->state.filename ) ) ) ) {
        return arg;
    }
    arg->stateNode = State::Help;
    return arg;
}

#endif
