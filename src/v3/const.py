MAXUSERFORTOUR = 2
MAXKMFORTOUR = 1330

FIXEDTOURCOST = 1000

KMFIXEDCOST = 1

STARTPLACE = 'roma'
ENDPLACE = STARTPLACE

PLACES = ["milano", "torino", "genova", "roma"]
          
DISTANCES = {
    "roma": {
        "milano":   346,
        "torino":   670,
        "genova":   500,
    },
    "milano": {
        "roma":     346,
        "torino":   143,
        "genova":   142,
    },
    "torino": {
        "roma":     670,
        "milano":   143,
        "genova":   172
    },
    "genova": {
        "roma":     500,
        "milano":   142,
        "torino":   172,
    }

}
