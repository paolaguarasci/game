MAXUSERFORTOUR = 2
MAXKMFORTOUR = 1330

FIXEDTOURCOST = 1000

KMFIXEDCOST = 1

STARTPLACE = 'roma'
ENDPLACE = STARTPLACE

PLACES = ["milano", "torino", "genova", "roma"]
COSTI =      {
    "roma": {
        "milano":   400,
        "torino":   450,
        "genova":   150,
    },
    "milano": {
        "roma":     400,
        "torino":   150,
        "genova":   200,
    },
    "torino": {
        "roma":     200,
        "milano":   150,
        "genova":   200
    },
    "genova": {
        "roma":     150,
        "milano":   200,
        "torino":   200,
    }}
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
