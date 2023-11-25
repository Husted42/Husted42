#include <stdbool.h>
#include <stdio.h>
#include <assert.h>

struct bit{
  bool v;
};


// bit: int -> bool
struct bit int_to_bool(int n) {
  struct bit myBit;
  if (n == 0) {
    myBit.v = false;
  } else if (n == 1) {
    myBit.v = true;
  } else {
    // assertion failure, terminates program
    assert(false);
  }
  return myBit;
}

