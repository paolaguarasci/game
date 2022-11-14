MAXUSERFORTOUR = 5
MAXKMFORTOUR = 4000
FIXEDTOURCOST = 1000

KMFIXEDCOST = 2

STARTPLACE = 'rome'
ENDPLACE = STARTPLACE

PLACES = ["rome", "paris", "vienna", "london",
          "brussels", "berlin", "amsterdam"]
          
DISTANCES = {
    "rome": {
        "rome": 0,
        "paris": 1419,
        "vienna": 1168,
        "london": 1867,
        "brussels": 1615,
        "berlin": 1508,
        "amsterdam": 1648,
    },
    "paris": {
        "rome": 1419,
        "paris": 0,
        "vienna": 1239,
        "london": 483,
        "brussels": 322,
        "berlin": 1054,
        "amsterdam": 507,
    },
    "vienna": {
        "rome": 1168,
        "paris": 1239,
        "vienna": 0,
        "london": 1471,
        "brussels": 1134,
        "berlin": 676,
        "amsterdam": 1147,
    },
    "london": {
        "rome": 1867,
        "paris": 483,
        "vienna": 1471,
        "london": 0,
        "brussels": 364,
        "berlin": 1094,
        "amsterdam": 533,
    },
    "brussels": {
        "rome": 1615,
        "paris": 322,
        "vienna": 1134,
        "london": 364,
        "brussels": 0,
        "berlin": 764,
        "amsterdam": 201,
    },
    "berlin": {
        "rome": 1508,
        "paris": 1054,
        "vienna": 676,
        "london": 1094,
        "brussels": 764,
        "berlin": 0,
        "amsterdam": 644,
    },
    "amsterdam": {
        "rome": 1648,
        "paris": 507,
        "vienna": 1147,
        "london": 533,
        "brussels": 201,
        "berlin": 644,
        "amsterdam": 0,
    },

}
