import math show PI

export *

abstract class MegaGreeter:
  names := []

  constructor name="World":
    names.add name

  say_hi:
    // Greet everyone individually!
    names.do: print "Hello $it!"
  say_bye a:
  	x := 1
    everyone := names.join ", "
    print "Bye $everyone, come back soon."
    return 1

main:
  greeter := MegaGreeter
  greeter.say_hi
  greeter.say_bye

  greeter.names.add "Lars"
  greeter.names.add "Kasper"
  greeter.names.add "Rikke"
  greeter.say_hi
  greeter.say_bye
