import os

# Default = False
debug                       = False

# A dictionary that maps strings (options) to integers (amounts of seconds)
duration_options    = {
      "short nap"   : 25  * 60
    , "long nap"    : 90  * 60
    , "short"       : 4.5 * 3600 + 5 * 60
    , "medium"      : 6   * 3600 + 5 * 60
    , "long"        : 7.5 * 3600 + 5 * 60
    , "very long"   : 9   * 3600 + 5 * 60
    , "crash"       : 12  * 3600
}

# Default = 60
pleasant_wake_up_volume     = 60 
