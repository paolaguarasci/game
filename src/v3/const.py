MAXUSERFORTOUR = 2
MAXKMFORTOUR = 350

FIXEDTOURCOST = 1000

KMFIXEDCOST = 1.5

STARTPLACE = 'bologna'
ENDPLACE = STARTPLACE

PLACES = ["milano", "torino", "genova"]
          
DISTANCES = {
    "bologna": {
        "milano": 213,
        "torino": 333,
        "genova": 299,
    },
    "milano": {
        "bologna": 213,
        "torino": 145,
        "genova": 150,
    },
    "torino": {
        "bologna": 333,
        "milano": 145,
        "genova": 172,
    },
    "genova": {
        "bologna": 299,
        "milano": 150,
        "torino": 172,
    }

}
