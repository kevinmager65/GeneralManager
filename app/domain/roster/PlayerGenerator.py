from app.domain.roster.Player import Player
from random import choice, randint


def generatePlayer(position,
                   minSpeed=1,
                   maxSpeed=100,
                   minStrength=1,
                   maxStrength=100,
                   minAbility=35,
                   maxAbility=100,
                   minAge=23,
                   maxAge=38
                   ):
    firstName = choice(__firstNames).lower().capitalize()
    lastName = choice(__lastName).lower().capitalize()

    speed = randint(minSpeed, maxSpeed)
    strength = randint(minStrength, maxStrength)
    position_ability = randint(minAbility, maxAbility)
    age = randint(minAge, maxAge)

    return Player(position, firstName, lastName, age,
                  speed, strength, position_ability)


def getPositionDefaults():
    return {
        'QB': {
            'count': 3,
            'abilities': {
                'maxSpeed': 50,
                'maxStrength': 50,
            }
        },
        'RB': {
            'count': 4,
            'abilities': {
                'minSpeed': 50
            }
        },
        'WR': {
            'count': 6,
            'abilities': {
                'minSpeed': 50
            }
        },
        'TE': {
            'count': 3,
            'abilities': {
                'maxSpeed': 75,
                'minSpeed': 25
            }
        },
        'OL': {
            'count': 9,
            'abilities': {
                'maxSpeed': 45,
                'minStrength': 50
            }
        },
        'DL': {
            'count': 9,
            'abilities': {
                'maxSpeed': 45,
                'minStrength': 50
            }
        },
        'LB': {
            'count': 9,
            'abilities': {
                'minSpeed': 33,
                'maxSpeed': 75,
                'minStrength': 33
            }
        },
        'DB': {
            'count': 10,
            'abilities': {
                'minSpeed': 50
            }
        },
        'K': {
            'count': 1,
            'abilities': {
                'maxSpeed': 10,
                'maxStrength': 15
            }
        },
        'P': {
            'count': 1,
            'abilities': {
                'maxSpeed': 10,
                'maxStrength': 15
            }
        }
    }


__firstNames = [
    "AARON",
    "ABDUL",
    "ABE",
    "ABEL",
    "ABRAHAM",
    "ABRAM",
    "ADALBERTO",
    "ADAM",
    "ADAN",
    "ADOLFO",
    "ADOLPH",
    "ADRIAN",
    "AGUSTIN",
    "AHMAD",
    "AHMED",
    "AL",
    "ALAN",
    "ALBERT",
    "ALBERTO",
    "ALDEN",
    "ALDO",
    "ALEC",
    "ALEJANDRO",
    "ALEX",
    "ALEXANDER",
    "ALEXIS",
    "ALFONSO",
    "ALFONZO",
    "ALFRED",
    "ALFREDO",
    "ALI",
    "ALLAN",
    "ALLEN",
    "ALONSO",
    "ALONZO",
    "ALPHONSE",
    "ALPHONSO",
    "ALTON",
    "ALVA",
    "ALVARO",
    "ALVIN",
    "AMADO",
    "AMBROSE",
    "AMOS",
    "ANDERSON",
    "ANDRE",
    "ANDREA",
    "ANDREAS",
    "ANDRES",
    "ANDREW",
    "ANDY",
    "ANGEL",
    "ANGELO",
    "ANIBAL",
    "ANTHONY",
    "ANTIONE",
    "ANTOINE",
    "ANTON",
    "ANTONE",
    "ANTONIA",
    "ANTONIO",
    "ANTONY",
    "ANTWAN",
    "ARCHIE",
    "ARDEN",
    "ARIEL",
    "ARLEN",
    "ARLIE",
    "ARMAND",
    "ARMANDO",
    "ARNOLD",
    "ARNOLDO",
    "ARNULFO",
    "ARON",
    "ARRON",
    "ART",
    "ARTHUR",
    "ARTURO",
    "ASA",
    "ASHLEY",
    "AUBREY",
    "AUGUST",
    "AUGUSTINE",
    "AUGUSTUS",
    "AURELIO",
    "AUSTIN",
    "AVERY",
    "BARNEY",
    "BARRETT",
    "BARRY",
    "BART",
    "BARTON",
    "BASIL",
    "BEAU",
    "BEN",
    "BENEDICT",
    "BENITO",
    "BENJAMIN",
    "BENNETT",
    "BENNIE",
    "BENNY",
    "BENTON",
    "BERNARD",
    "BERNARDO",
    "BERNIE",
    "BERRY",
    "BERT",
    "BERTRAM",
    "BILL",
    "BILLIE",
    "BILLY",
    "BLAINE",
    "BLAIR",
    "BLAKE",
    "BO",
    "BOB",
    "BOBBIE",
    "BOBBY",
    "BOOKER",
    "BORIS",
    "BOYCE",
    "BOYD",
    "BRAD",
    "BRADFORD",
    "BRADLEY",
    "BRADLY",
    "BRADY",
    "BRAIN",
    "BRANDEN",
    "BRANDON",
    "BRANT",
    "BRENDAN",
    "BRENDON",
    "BRENT",
    "BRENTON",
    "BRET",
    "BRETT",
    "BRIAN",
    "BRICE",
    "BRITT",
    "BROCK",
    "BRODERICK",
    "BROOKS",
    "BRUCE",
    "BRUNO",
    "BRYAN",
    "BRYANT",
    "BRYCE",
    "BRYON",
    "BUCK",
    "BUD",
    "BUDDY",
    "BUFORD",
    "BURL",
    "BURT",
    "BURTON",
    "BUSTER",
    "BYRON",
    "CALEB",
    "CALVIN",
    "CAMERON",
    "CAREY",
    "CARL",
    "CARLO",
    "CARLOS",
    "CARLTON",
    "CARMELO",
    "CARMEN",
    "CARMINE",
    "CAROL",
    "CARROL",
    "CARROLL",
    "CARSON",
    "CARTER",
    "CARY",
    "CASEY",
    "CECIL",
    "CEDRIC",
    "CEDRICK",
    "CESAR",
    "CHAD",
    "CHADWICK",
    "CHANCE",
    "CHANG",
    "CHARLES",
    "CHARLEY",
    "CHARLIE",
    "CHAS",
    "CHASE",
    "CHAUNCEY",
    "CHESTER",
    "CHET",
    "CHI",
    "CHONG",
    "CHRIS",
    "CHRISTIAN",
    "CHRISTOPER",
    "CHRISTOPHER",
    "CHUCK",
    "CHUNG",
    "CLAIR",
    "CLARENCE",
    "CLARK",
    "CLAUD",
    "CLAUDE",
    "CLAUDIO",
    "CLAY",
    "CLAYTON",
    "CLEMENT",
    "CLEMENTE",
    "CLEO",
    "CLETUS",
    "CLEVELAND",
    "CLIFF",
    "CLIFFORD",
    "CLIFTON",
    "CLINT",
    "CLINTON",
    "CLYDE",
    "CODY",
    "COLBY",
    "COLE",
    "COLEMAN",
    "COLIN",
    "COLLIN",
    "COLTON",
    "COLUMBUS",
    "CONNIE",
    "CONRAD",
    "CORDELL",
    "COREY",
    "CORNELIUS",
    "CORNELL",
    "CORTEZ",
    "CORY",
    "COURTNEY",
    "COY",
    "CRAIG",
    "CRISTOBAL",
    "CRISTOPHER",
    "CRUZ",
    "CURT",
    "CURTIS",
    "CYRIL",
    "CYRUS",
    "DALE",
    "DALLAS",
    "DALTON",
    "DAMIAN",
    "DAMIEN",
    "DAMION",
    "DAMON",
    "DAN",
    "DANA",
    "DANE",
    "DANIAL",
    "DANIEL",
    "DANILO",
    "DANNIE",
    "DANNY",
    "DANTE",
    "DARELL",
    "DAREN",
    "DARIN",
    "DARIO",
    "DARIUS",
    "DARNELL",
    "DARON",
    "DARREL",
    "DARRELL",
    "DARREN",
    "DARRICK",
    "DARRIN",
    "DARRON",
    "DARRYL",
    "DARWIN",
    "DARYL",
    "DAVE",
    "DAVID",
    "DAVIS",
    "DEAN",
    "DEANDRE",
    "DEANGELO",
    "DEE",
    "DEL",
    "DELBERT",
    "DELMAR",
    "DELMER",
    "DEMARCUS",
    "DEMETRIUS",
    "DENIS",
    "DENNIS",
    "DENNY",
    "DENVER",
    "DEON",
    "DEREK",
    "DERICK",
    "DERRICK",
    "DESHAWN",
    "DESMOND",
    "DEVIN",
    "DEVON",
    "DEWAYNE",
    "DEWEY",
    "DEWITT",
    "DEXTER",
    "DICK",
    "DIEGO",
    "DILLON",
    "DINO",
    "DION",
    "DIRK",
    "DOMENIC",
    "DOMINGO",
    "DOMINIC",
    "DOMINICK",
    "DOMINIQUE",
    "DON",
    "DONALD",
    "DONG",
    "DONN",
    "DONNELL",
    "DONNIE",
    "DONNY",
    "DONOVAN",
    "DONTE",
    "DORIAN",
    "DORSEY",
    "DOUG",
    "DOUGLAS",
    "DOUGLASS",
    "DOYLE",
    "DREW",
    "DUANE",
    "DUDLEY",
    "DUNCAN",
    "DUSTIN",
    "DUSTY",
    "DWAIN",
    "DWAYNE",
    "DWIGHT",
    "DYLAN",
    "EARL",
    "EARLE",
    "EARNEST",
    "ED",
    "EDDIE",
    "EDDY",
    "EDGAR",
    "EDGARDO",
    "EDISON",
    "EDMOND",
    "EDMUND",
    "EDMUNDO",
    "EDUARDO",
    "EDWARD",
    "EDWARDO",
    "EDWIN",
    "EFRAIN",
    "EFREN",
    "ELBERT",
    "ELDEN",
    "ELDON",
    "ELDRIDGE",
    "ELI",
    "ELIAS",
    "ELIJAH",
    "ELISEO",
    "ELISHA",
    "ELLIOT",
    "ELLIOTT",
    "ELLIS",
    "ELLSWORTH",
    "ELMER",
    "ELMO",
    "ELOY",
    "ELROY",
    "ELTON",
    "ELVIN",
    "ELVIS",
    "ELWOOD",
    "EMANUEL",
    "EMERSON",
    "EMERY",
    "EMIL",
    "EMILE",
    "EMILIO",
    "EMMANUEL",
    "EMMETT",
    "EMMITT",
    "EMORY",
    "ENOCH",
    "ENRIQUE",
    "ERASMO",
    "ERIC",
    "ERICH",
    "ERICK",
    "ERIK",
    "ERIN",
    "ERNEST",
    "ERNESTO",
    "ERNIE",
    "ERROL",
    "ERVIN",
    "ERWIN",
    "ESTEBAN",
    "ETHAN",
    "EUGENE",
    "EUGENIO",
    "EUSEBIO",
    "EVAN",
    "EVERETT",
    "EVERETTE",
    "EZEKIEL",
    "EZEQUIEL",
    "EZRA",
    "FABIAN",
    "FAUSTINO",
    "FAUSTO",
    "FEDERICO",
    "FELIPE",
    "FELIX",
    "FELTON",
    "FERDINAND",
    "FERMIN",
    "FERNANDO",
    "FIDEL",
    "FILIBERTO",
    "FLETCHER",
    "FLORENCIO",
    "FLORENTINO",
    "FLOYD",
    "FOREST",
    "FORREST",
    "FOSTER",
    "FRANCES",
    "FRANCESCO",
    "FRANCIS",
    "FRANCISCO",
    "FRANK",
    "FRANKIE",
    "FRANKLIN",
    "FRANKLYN",
    "FRED",
    "FREDDIE",
    "FREDDY",
    "FREDERIC",
    "FREDERICK",
    "FREDRIC",
    "FREDRICK",
    "FREEMAN",
    "FRITZ",
    "GABRIEL",
    "GAIL",
    "GALE",
    "GALEN",
    "GARFIELD",
    "GARLAND",
    "GARRET",
    "GARRETT",
    "GARRY",
    "GARTH",
    "GARY",
    "GASTON",
    "GAVIN",
    "GAYLE",
    "GAYLORD",
    "GENARO",
    "GENE",
    "GEOFFREY",
    "GEORGE",
    "GERALD",
    "GERALDO",
    "GERARD",
    "GERARDO",
    "GERMAN",
    "GERRY",
    "GIL",
    "GILBERT",
    "GILBERTO",
    "GINO",
    "GIOVANNI",
    "GIUSEPPE",
    "GLEN",
    "GLENN",
    "GONZALO",
    "GORDON",
    "GRADY",
    "GRAHAM",
    "GRAIG",
    "GRANT",
    "GRANVILLE",
    "GREG",
    "GREGG",
    "GREGORIO",
    "GREGORY",
    "GROVER",
    "GUADALUPE",
    "GUILLERMO",
    "GUS",
    "GUSTAVO",
    "GUY",
    "HAI",
    "HAL",
    "HANK",
    "HANS",
    "HARLAN",
    "HARLAND",
    "HARLEY",
    "HAROLD",
    "HARRIS",
    "HARRISON",
    "HARRY",
    "HARVEY",
    "HASSAN",
    "HAYDEN",
    "HAYWOOD",
    "HEATH",
    "HECTOR",
    "HENRY",
    "HERB",
    "HERBERT",
    "HERIBERTO",
    "HERMAN",
    "HERSCHEL",
    "HERSHEL",
    "HILARIO",
    "HILTON",
    "HIPOLITO",
    "HIRAM",
    "HOBERT",
    "HOLLIS",
    "HOMER",
    "HONG",
    "HORACE",
    "HORACIO",
    "HOSEA",
    "HOUSTON",
    "HOWARD",
    "HOYT",
    "HUBERT",
    "HUEY",
    "HUGH",
    "HUGO",
    "HUMBERTO",
    "HUNG",
    "HUNTER",
    "HYMAN",
    "IAN",
    "IGNACIO",
    "IKE",
    "IRA",
    "IRVIN",
    "IRVING",
    "IRWIN",
    "ISAAC",
    "ISAIAH",
    "ISAIAS",
    "ISIAH",
    "ISIDRO",
    "ISMAEL",
    "ISRAEL",
    "ISREAL",
    "ISSAC",
    "IVAN",
    "IVORY",
    "JACINTO",
    "JACK",
    "JACKIE",
    "JACKSON",
    "JACOB",
    "JACQUES",
    "JAE",
    "JAIME",
    "JAKE",
    "JAMAAL",
    "JAMAL",
    "JAMAR",
    "JAME",
    "JAMEL",
    "JAMES",
    "JAMEY",
    "JAMIE",
    "JAMISON",
    "JAN",
    "JARED",
    "JAROD",
    "JARRED",
    "JARRETT",
    "JARROD",
    "JARVIS",
    "JASON",
    "JASPER",
    "JAVIER",
    "JAY",
    "JAYSON",
    "JC",
    "JEAN",
    "JED",
    "JEFF",
    "JEFFEREY",
    "JEFFERSON",
    "JEFFERY",
    "JEFFREY",
    "JEFFRY",
    "JERALD",
    "JERAMY",
    "JERE",
    "JEREMIAH",
    "JEREMY",
    "JERMAINE",
    "JEROLD",
    "JEROME",
    "JEROMY",
    "JERRELL",
    "JERROD",
    "JERROLD",
    "JERRY",
    "JESS",
    "JESSE",
    "JESSIE",
    "JESUS",
    "JEWEL",
    "JEWELL",
    "JIM",
    "JIMMIE",
    "JIMMY",
    "JOAN",
    "JOAQUIN",
    "JODY",
    "JOE",
    "JOEL",
    "JOESPH",
    "JOEY",
    "JOHN",
    "JOHNATHAN",
    "JOHNATHON",
    "JOHNIE",
    "JOHNNIE",
    "JOHNNY",
    "JOHNSON",
    "JON",
    "JONAH",
    "JONAS",
    "JONATHAN",
    "JONATHON",
    "JORDAN",
    "JORDON",
    "JORGE",
    "JOSE",
    "JOSEF",
    "JOSEPH",
    "JOSH",
    "JOSHUA",
    "JOSIAH",
    "JOSPEH",
    "JOSUE",
    "JUAN",
    "JUDE",
    "JUDSON",
    "JULES",
    "JULIAN",
    "JULIO",
    "JULIUS",
    "JUNIOR",
    "JUSTIN",
    "KAREEM",
    "KARL",
    "KASEY",
    "KEENAN",
    "KEITH",
    "KELLEY",
    "KELLY",
    "KELVIN",
    "KEN",
    "KENDALL",
    "KENDRICK",
    "KENETH",
    "KENNETH",
    "KENNITH",
    "KENNY",
    "KENT",
    "KENTON",
    "KERMIT",
    "KERRY",
    "KEVEN",
    "KEVIN",
    "KIETH",
    "KIM",
    "KING",
    "KIP",
    "KIRBY",
    "KIRK",
    "KOREY",
    "KORY",
    "KRAIG",
    "KRIS",
    "KRISTOFER",
    "KRISTOPHER",
    "KURT",
    "KURTIS",
    "KYLE",
    "LACY",
    "LAMAR",
    "LAMONT",
    "LANCE",
    "LANDON",
    "LANE",
    "LANNY",
    "LARRY",
    "LAUREN",
    "LAURENCE",
    "LAVERN",
    "LAVERNE",
    "LAWERENCE",
    "LAWRENCE",
    "LAZARO",
    "LEANDRO",
    "LEE",
    "LEIF",
    "LEIGH",
    "LELAND",
    "LEMUEL",
    "LEN",
    "LENARD",
    "LENNY",
    "LEO",
    "LEON",
    "LEONARD",
    "LEONARDO",
    "LEONEL",
    "LEOPOLDO",
    "LEROY",
    "LES",
    "LESLEY",
    "LESLIE",
    "LESTER",
    "LEVI",
    "LEWIS",
    "LINCOLN",
    "LINDSAY",
    "LINDSEY",
    "LINO",
    "LINWOOD",
    "LIONEL",
    "LLOYD",
    "LOGAN",
    "LON",
    "LONG",
    "LONNIE",
    "LONNY",
    "LOREN",
    "LORENZO",
    "LOU",
    "LOUIE",
    "LOUIS",
    "LOWELL",
    "LOYD",
    "LUCAS",
    "LUCIANO",
    "LUCIEN",
    "LUCIO",
    "LUCIUS",
    "LUIGI",
    "LUIS",
    "LUKE",
    "LUPE",
    "LUTHER",
    "LYLE",
    "LYMAN",
    "LYNDON",
    "LYNN",
    "LYNWOOD",
    "MAC",
    "MACK",
    "MAJOR",
    "MALCOLM",
    "MALCOM",
    "MALIK",
    "MAN",
    "MANUAL",
    "MANUEL",
    "MARC",
    "MARCEL",
    "MARCELINO",
    "MARCELLUS",
    "MARCELO",
    "MARCO",
    "MARCOS",
    "MARCUS",
    "MARGARITO",
    "MARIA",
    "MARIANO",
    "MARIO",
    "MARION",
    "MARK",
    "MARKUS",
    "MARLIN",
    "MARLON",
    "MARQUIS",
    "MARSHALL",
    "MARTIN",
    "MARTY",
    "MARVIN",
    "MARY",
    "MASON",
    "MATHEW",
    "MATT",
    "MATTHEW",
    "MAURICE",
    "MAURICIO",
    "MAURO",
    "MAX",
    "MAXIMO",
    "MAXWELL",
    "MAYNARD",
    "MCKINLEY",
    "MEL",
    "MELVIN",
    "MERLE",
    "MERLIN",
    "MERRILL",
    "MERVIN",
    "MICAH",
    "MICHAEL",
    "MICHAL",
    "MICHALE",
    "MICHEAL",
    "MICHEL",
    "MICKEY",
    "MIGUEL",
    "MIKE",
    "MIKEL",
    "MILAN",
    "MILES",
    "MILFORD",
    "MILLARD",
    "MILO",
    "MILTON",
    "MINH",
    "MIQUEL",
    "MITCH",
    "MITCHEL",
    "MITCHELL",
    "MODESTO",
    "MOHAMED",
    "MOHAMMAD",
    "MOHAMMED",
    "MOISES",
    "MONROE",
    "MONTE",
    "MONTY",
    "MORGAN",
    "MORRIS",
    "MORTON",
    "MOSE",
    "MOSES",
    "MOSHE",
    "MURRAY",
    "MYLES",
    "MYRON",
    "NAPOLEON",
    "NATHAN",
    "NATHANAEL",
    "NATHANIAL",
    "NATHANIEL",
    "NEAL",
    "NED",
    "NEIL",
    "NELSON",
    "NESTOR",
    "NEVILLE",
    "NEWTON",
    "NICHOLAS",
    "NICK",
    "NICKOLAS",
    "NICKY",
    "NICOLAS",
    "NIGEL",
    "NOAH",
    "NOBLE",
    "NOE",
    "NOEL",
    "NOLAN",
    "NORBERT",
    "NORBERTO",
    "NORMAN",
    "NORMAND",
    "NORRIS",
    "NUMBERS",
    "OCTAVIO",
    "ODELL",
    "ODIS",
    "OLEN",
    "OLIN",
    "OLIVER",
    "OLLIE",
    "OMAR",
    "OMER",
    "OREN",
    "ORLANDO",
    "ORVAL",
    "ORVILLE",
    "OSCAR",
    "OSVALDO",
    "OSWALDO",
    "OTHA",
    "OTIS",
    "OTTO",
    "OWEN",
    "PABLO",
    "PALMER",
    "PARIS",
    "PARKER",
    "PASQUALE",
    "PAT",
    "PATRICIA",
    "PATRICK",
    "PAUL",
    "PEDRO",
    "PERCY",
    "PERRY",
    "PETE",
    "PETER",
    "PHIL",
    "PHILIP",
    "PHILLIP",
    "PIERRE",
    "PORFIRIO",
    "PORTER",
    "PRESTON",
    "PRINCE",
    "QUENTIN",
    "QUINCY",
    "QUINN",
    "QUINTIN",
    "QUINTON",
    "RAFAEL",
    "RALEIGH",
    "RALPH",
    "RAMIRO",
    "RAMON",
    "RANDAL",
    "RANDALL",
    "RANDELL",
    "RANDOLPH",
    "RANDY",
    "RAPHAEL",
    "RASHAD",
    "RAUL",
    "RAY",
    "RAYFORD",
    "RAYMON",
    "RAYMOND",
    "RAYMUNDO",
    "REED",
    "REFUGIO",
    "REGGIE",
    "REGINALD",
    "REID",
    "REINALDO",
    "RENALDO",
    "RENATO",
    "RENE",
    "REUBEN",
    "REX",
    "REY",
    "REYES",
    "REYNALDO",
    "RHETT",
    "RICARDO",
    "RICH",
    "RICHARD",
    "RICHIE",
    "RICK",
    "RICKEY",
    "RICKIE",
    "RICKY",
    "RICO",
    "RIGOBERTO",
    "RILEY",
    "ROB",
    "ROBBIE",
    "ROBBY",
    "ROBERT",
    "ROBERTO",
    "ROBIN",
    "ROBT",
    "ROCCO",
    "ROCKY",
    "ROD",
    "RODERICK",
    "RODGER",
    "RODNEY",
    "RODOLFO",
    "RODRICK",
    "RODRIGO",
    "ROGELIO",
    "ROGER",
    "ROLAND",
    "ROLANDO",
    "ROLF",
    "ROLLAND",
    "ROMAN",
    "ROMEO",
    "RON",
    "RONALD",
    "RONNIE",
    "RONNY",
    "ROOSEVELT",
    "RORY",
    "ROSARIO",
    "ROSCOE",
    "ROSENDO",
    "ROSS",
    "ROY",
    "ROYAL",
    "ROYCE",
    "RUBEN",
    "RUBIN",
    "RUDOLF",
    "RUDOLPH",
    "RUDY",
    "RUEBEN",
    "RUFUS",
    "RUPERT",
    "RUSS",
    "RUSSEL",
    "RUSSELL",
    "RUSTY",
    "RYAN",
    "SAL",
    "SALVADOR",
    "SALVATORE",
    "SAM",
    "SAMMIE",
    "SAMMY",
    "SAMUAL",
    "SAMUEL",
    "SANDY",
    "SANFORD",
    "SANG",
    "SANTIAGO",
    "SANTO",
    "SANTOS",
    "SAUL",
    "SCOT",
    "SCOTT",
    "SCOTTIE",
    "SCOTTY",
    "SEAN",
    "SEBASTIAN",
    "SERGIO",
    "SETH",
    "SEYMOUR",
    "SHAD",
    "SHANE",
    "SHANNON",
    "SHAUN",
    "SHAWN",
    "SHAYNE",
    "SHELBY",
    "SHELDON",
    "SHELTON",
    "SHERMAN",
    "SHERWOOD",
    "SHIRLEY",
    "SHON",
    "SID",
    "SIDNEY",
    "SILAS",
    "SIMON",
    "SOL",
    "SOLOMON",
    "SON",
    "SONNY",
    "SPENCER",
    "STACEY",
    "STACY",
    "STAN",
    "STANFORD",
    "STANLEY",
    "STANTON",
    "STEFAN",
    "STEPHAN",
    "STEPHEN",
    "STERLING",
    "STEVE",
    "STEVEN",
    "STEVIE",
    "STEWART",
    "STUART",
    "SUNG",
    "SYDNEY",
    "SYLVESTER",
    "TAD",
    "TANNER",
    "TAYLOR",
    "TED",
    "TEDDY",
    "TEODORO",
    "TERENCE",
    "TERRANCE",
    "TERRELL",
    "TERRENCE",
    "TERRY",
    "THAD",
    "THADDEUS",
    "THANH",
    "THEO",
    "THEODORE",
    "THERON",
    "THOMAS",
    "THURMAN",
    "TIM",
    "TIMMY",
    "TIMOTHY",
    "TITUS",
    "TOBIAS",
    "TOBY",
    "TOD",
    "TODD",
    "TOM",
    "TOMAS",
    "TOMMIE",
    "TOMMY",
    "TONEY",
    "TONY",
    "TORY",
    "TRACEY",
    "TRACY",
    "TRAVIS",
    "TRENT",
    "TRENTON",
    "TREVOR",
    "TREY",
    "TRINIDAD",
    "TRISTAN",
    "TROY",
    "TRUMAN",
    "TUAN",
    "TY",
    "TYLER",
    "TYREE",
    "TYRELL",
    "TYRON",
    "TYRONE",
    "TYSON",
    "ULYSSES",
    "VAL",
    "VALENTIN",
    "VALENTINE",
    "VAN",
    "VANCE",
    "VAUGHN",
    "VERN",
    "VERNON",
    "VICENTE",
    "VICTOR",
    "VINCE",
    "VINCENT",
    "VINCENZO",
    "VIRGIL",
    "VIRGILIO",
    "VITO",
    "VON",
    "WADE",
    "WALDO",
    "WALKER",
    "WALLACE",
    "WALLY",
    "WALTER",
    "WALTON",
    "WARD",
    "WARNER",
    "WARREN",
    "WAYLON",
    "WAYNE",
    "WELDON",
    "WENDELL",
    "WERNER",
    "WES",
    "WESLEY",
    "WESTON",
    "WHITNEY",
    "WILBER",
    "WILBERT",
    "WILBUR",
    "WILBURN",
    "WILEY",
    "WILFORD",
    "WILFRED",
    "WILFREDO",
    "WILL",
    "WILLARD",
    "WILLIAM",
    "WILLIAMS",
    "WILLIAN",
    "WILLIE",
    "WILLIS",
    "WILLY",
    "WILMER",
    "WILSON",
    "WILTON",
    "WINFORD",
    "WINFRED",
    "WINSTON",
    "WM",
    "WOODROW",
    "WYATT",
    "XAVIER",
    "YONG",
    "YOUNG",
    "ZACHARIAH",
    "ZACHARY",
    "ZACHERY",
    "ZACK",
    "ZACKARY",
    "ZANE"
    ]

__lastName = [
    "SMITH",
    "JOHNSON",
    "WILLIAMS",
    "BROWN",
    "JONES",
    "MILLER",
    "DAVIS",
    "GARCIA",
    "RODRIGUEZ",
    "WILSON",
    "MARTINEZ",
    "ANDERSON",
    "TAYLOR",
    "THOMAS",
    "HERNANDEZ",
    "MOORE",
    "MARTIN",
    "JACKSON",
    "THOMPSON",
    "WHITE",
    "LOPEZ",
    "LEE",
    "GONZALEZ",
    "HARRIS",
    "CLARK",
    "LEWIS",
    "ROBINSON",
    "WALKER",
    "PEREZ",
    "HALL",
    "YOUNG",
    "ALLEN",
    "SANCHEZ",
    "WRIGHT",
    "KING",
    "SCOTT",
    "GREEN",
    "BAKER",
    "ADAMS",
    "NELSON",
    "HILL",
    "RAMIREZ",
    "CAMPBELL",
    "MITCHELL",
    "ROBERTS",
    "CARTER",
    "PHILLIPS",
    "EVANS",
    "TURNER",
    "TORRES",
    "PARKER",
    "COLLINS",
    "EDWARDS",
    "STEWART",
    "FLORES",
    "MORRIS",
    "NGUYEN",
    "MURPHY",
    "RIVERA",
    "COOK",
    "ROGERS",
    "MORGAN",
    "PETERSON",
    "COOPER",
    "REED",
    "BAILEY",
    "BELL",
    "GOMEZ",
    "KELLY",
    "HOWARD",
    "WARD",
    "COX",
    "DIAZ",
    "RICHARDSON",
    "WOOD",
    "WATSON",
    "BROOKS",
    "BENNETT",
    "GRAY",
    "JAMES",
    "REYES",
    "CRUZ",
    "HUGHES",
    "PRICE",
    "MYERS",
    "LONG",
    "FOSTER",
    "SANDERS",
    "ROSS",
    "MORALES",
    "POWELL",
    "SULLIVAN",
    "RUSSELL",
    "ORTIZ",
    "JENKINS",
    "GUTIERREZ",
    "PERRY",
    "BUTLER",
    "BARNES",
    "FISHER",
    "HENDERSON",
    "COLEMAN",
    "SIMMONS",
    "PATTERSON",
    "JORDAN",
    "REYNOLDS",
    "HAMILTON",
    "GRAHAM",
    "KIM",
    "GONZALES",
    "ALEXANDER",
    "RAMOS",
    "WALLACE",
    "GRIFFIN",
    "WEST",
    "COLE",
    "HAYES",
    "CHAVEZ",
    "GIBSON",
    "BRYANT",
    "ELLIS",
    "STEVENS",
    "MURRAY",
    "FORD",
    "MARSHALL",
    "OWENS",
    "MCDONALD",
    "HARRISON",
    "RUIZ",
    "KENNEDY",
    "WELLS",
    "ALVAREZ",
    "WOODS",
    "MENDOZA",
    "CASTILLO",
    "OLSON",
    "WEBB",
    "WASHINGTON",
    "TUCKER",
    "FREEMAN",
    "BURNS",
    "HENRY",
    "VASQUEZ",
    "SNYDER",
    "SIMPSON",
    "CRAWFORD",
    "JIMENEZ",
    "PORTER",
    "MASON",
    "SHAW",
    "GORDON",
    "WAGNER",
    "HUNTER",
    "ROMERO",
    "HICKS",
    "DIXON",
    "HUNT",
    "PALMER",
    "ROBERTSON",
    "BLACK",
    "HOLMES",
    "STONE",
    "MEYER",
    "BOYD",
    "MILLS",
    "WARREN",
    "FOX",
    "ROSE",
    "RICE",
    "MORENO",
    "SCHMIDT",
    "PATEL",
    "FERGUSON",
    "NICHOLS",
    "HERRERA",
    "MEDINA",
    "RYAN",
    "FERNANDEZ",
    "WEAVER",
    "DANIELS",
    "STEPHENS",
    "GARDNER",
    "PAYNE",
    "KELLEY",
    "DUNN",
    "PIERCE",
    "ARNOLD",
    "TRAN",
    "SPENCER",
    "PETERS",
    "HAWKINS",
    "GRANT",
    "HANSEN",
    "CASTRO",
    "HOFFMAN",
    "HART",
    "ELLIOTT",
    "CUNNINGHAM",
    "KNIGHT",
    "BRADLEY",
    "CARROLL",
    "HUDSON",
    "DUNCAN",
    "ARMSTRONG",
    "BERRY",
    "ANDREWS",
    "JOHNSTON",
    "RAY",
    "LANE",
    "RILEY",
    "CARPENTER",
    "PERKINS",
    "AGUILAR",
    "SILVA",
    "RICHARDS",
    "WILLIS",
    "MATTHEWS",
    "CHAPMAN",
    "LAWRENCE",
    "GARZA",
    "VARGAS",
    "WATKINS",
    "WHEELER",
    "LARSON",
    "CARLSON",
    "HARPER",
    "GEORGE",
    "GREENE",
    "BURKE",
    "GUZMAN",
    "MORRISON",
    "MUNOZ",
    "JACOBS",
    "OBRIEN",
    "LAWSON",
    "FRANKLIN",
    "LYNCH",
    "BISHOP",
    "CARR",
    "SALAZAR",
    "AUSTIN",
    "MENDEZ",
    "GILBERT",
    "JENSEN",
    "WILLIAMSON",
    "MONTGOMERY",
    "HARVEY",
    "OLIVER",
    "HOWELL",
    "DEAN",
    "HANSON",
    "WEBER",
    "GARRETT",
    "SIMS",
    "BURTON",
    "FULLER",
    "SOTO",
    "MCCOY",
    "WELCH",
    "CHEN",
    "SCHULTZ",
    "WALTERS",
    "REID",
    "FIELDS",
    "WALSH",
    "LITTLE",
    "FOWLER",
    "BOWMAN",
    "DAVIDSON",
    "MAY",
    "DAY",
    "SCHNEIDER",
    "NEWMAN",
    "BREWER",
    "LUCAS",
    "HOLLAND",
    "WONG",
    "BANKS",
    "SANTOS",
    "CURTIS",
    "PEARSON",
    "DELGADO",
    "VALDEZ",
    "PENA",
    "RIOS",
    "DOUGLAS",
    "SANDOVAL",
    "BARRETT",
    "HOPKINS",
    "KELLER",
    "GUERRERO",
    "STANLEY",
    "BATES",
    "ALVARADO",
    "BECK",
    "ORTEGA",
    "WADE",
    "ESTRADA",
    "CONTRERAS",
    "BARNETT",
    "CALDWELL",
    "SANTIAGO",
    "LAMBERT",
    "POWERS",
    "CHAMBERS",
    "NUNEZ",
    "CRAIG",
    "LEONARD",
    "LOWE",
    "RHODES",
    "BYRD",
    "GREGORY",
    "SHELTON",
    "FRAZIER",
    "BECKER",
    "MALDONADO",
    "FLEMING",
    "VEGA",
    "SUTTON",
    "COHEN",
    "JENNINGS",
    "PARKS",
    "MCDANIEL",
    "WATTS",
    "BARKER",
    "NORRIS",
    "VAUGHN",
    "VAZQUEZ",
    "HOLT",
    "SCHWARTZ",
    "STEELE",
    "BENSON",
    "NEAL",
    "DOMINGUEZ",
    "HORTON",
    "TERRY",
    "WOLFE",
    "HALE",
    "LYONS",
    "GRAVES",
    "HAYNES",
    "MILES",
    "PARK",
    "WARNER",
    "PADILLA",
    "BUSH",
    "THORNTON",
    "MCCARTHY",
    "MANN",
    "ZIMMERMAN",
    "ERICKSON",
    "FLETCHER",
    "MCKINNEY",
    "PAGE",
    "DAWSON",
    "JOSEPH",
    "MARQUEZ",
    "REEVES",
    "KLEIN",
    "ESPINOZA",
    "BALDWIN",
    "MORAN",
    "LOVE",
    "ROBBINS",
    "HIGGINS",
    "BALL",
    "CORTEZ",
    "LE",
    "GRIFFITH",
    "BOWEN",
    "SHARP",
    "CUMMINGS",
    "RAMSEY",
    "HARDY",
    "SWANSON",
    "BARBER",
    "ACOSTA",
    "LUNA",
    "CHANDLER",
    "DANIEL",
    "BLAIR",
    "CROSS",
    "SIMON",
    "DENNIS",
    "OCONNOR",
    "QUINN",
    "GROSS",
    "NAVARRO",
    "MOSS",
    "FITZGERALD",
    "DOYLE",
    "MCLAUGHLIN",
    "ROJAS",
    "RODGERS",
    "STEVENSON",
    "SINGH",
    "YANG",
    "FIGUEROA",
    "HARMON",
    "NEWTON",
    "PAUL",
    "MANNING",
    "GARNER",
    "MCGEE",
    "REESE",
    "FRANCIS",
    "BURGESS",
    "ADKINS",
    "GOODMAN",
    "CURRY",
    "BRADY",
    "CHRISTENSEN",
    "POTTER",
    "WALTON",
    "GOODWIN",
    "MULLINS",
    "MOLINA",
    "WEBSTER",
    "FISCHER",
    "CAMPOS",
    "AVILA",
    "SHERMAN",
    "TODD",
    "CHANG",
    "BLAKE",
    "MALONE",
    "WOLF",
    "HODGES",
    "JUAREZ",
    "GILL",
    "FARMER",
    "HINES",
    "GALLAGHER",
    "DURAN",
    "HUBBARD",
    "CANNON",
    "MIRANDA",
    "WANG",
    "SAUNDERS",
    "TATE",
    "MACK",
    "HAMMOND",
    "CARRILLO",
    "TOWNSEND",
    "WISE",
    "INGRAM",
    "BARTON",
    "MEJIA",
    "AYALA",
    "SCHROEDER",
    "HAMPTON",
    "ROWE",
    "PARSONS",
    "FRANK",
    "WATERS",
    "STRICKLAND",
    "OSBORNE",
    "MAXWELL",
    "CHAN",
    "DELEON",
    "NORMAN",
    "HARRINGTON",
    "CASEY",
    "PATTON",
    "LOGAN",
    "BOWERS",
    "MUELLER",
    "GLOVER",
    "FLOYD",
    "HARTMAN",
    "BUCHANAN",
    "COBB",
    "FRENCH",
    "KRAMER",
    "MCCORMICK",
    "CLARKE",
    "TYLER",
    "GIBBS",
    "MOODY",
    "CONNER",
    "SPARKS",
    "MCGUIRE",
    "LEON",
    "BAUER",
    "NORTON",
    "POPE",
    "FLYNN",
    "HOGAN",
    "ROBLES",
    "SALINAS",
    "YATES",
    "LINDSEY",
    "LLOYD",
    "MARSH",
    "MCBRIDE",
    "OWEN",
    "SOLIS",
    "PHAM",
    "LANG",
    "PRATT",
    "LARA",
    "BROCK",
    "BALLARD",
    "TRUJILLO",
    "SHAFFER",
    "DRAKE",
    "ROMAN",
    "AGUIRRE",
    "MORTON",
    "STOKES",
    "LAMB",
    "PACHECO",
    "PATRICK",
    "COCHRAN",
    "SHEPHERD",
    "CAIN",
    "BURNETT",
    "HESS",
    "LI",
    "CERVANTES",
    "OLSEN",
    "BRIGGS",
    "OCHOA",
    "CABRERA",
    "VELASQUEZ",
    "MONTOYA",
    "ROTH",
    "MEYERS",
    "CARDENAS",
    "FUENTES",
    "WEISS",
    "WILKINS",
    "HOOVER",
    "NICHOLSON",
    "UNDERWOOD",
    "SHORT",
    "CARSON",
    "MORROW",
    "COLON",
    "HOLLOWAY",
    "SUMMERS",
    "BRYAN",
    "PETERSEN",
    "MCKENZIE",
    "SERRANO",
    "WILCOX",
    "CAREY",
    "CLAYTON",
    "POOLE",
    "CALDERON",
    "GALLEGOS",
    "GREER",
    "RIVAS",
    "GUERRA",
    "DECKER",
    "COLLIER",
    "WALL",
    "WHITAKER",
    "BASS",
    "FLOWERS",
    "DAVENPORT",
    "CONLEY",
    "HOUSTON",
    "HUFF",
    "COPELAND",
    "HOOD",
    "MONROE",
    "MASSEY",
    "ROBERSON",
    "COMBS",
    "FRANCO",
    "LARSEN",
    "PITTMAN",
    "RANDALL",
    "SKINNER",
    "WILKINSON",
    "KIRBY",
    "CAMERON",
    "BRIDGES",
    "ANTHONY",
    "RICHARD",
    "KIRK",
    "BRUCE",
    "SINGLETON",
    "MATHIS",
    "BRADFORD",
    "BOONE",
    "ABBOTT",
    "CHARLES",
    "ALLISON",
    "SWEENEY",
    "ATKINSON",
    "HORN",
    "JEFFERSON",
    "ROSALES",
    "YORK",
    "CHRISTIAN",
    "PHELPS",
    "FARRELL",
    "CASTANEDA",
    "NASH",
    "DICKERSON",
    "BOND",
    "WYATT",
    "FOLEY",
    "CHASE",
    "GATES",
    "VINCENT",
    "MATHEWS",
    "HODGE",
    "GARRISON",
    "TREVINO",
    "VILLARREAL",
    "HEATH",
    "DALTON",
    "VALENCIA",
    "CALLAHAN",
    "HENSLEY",
    "ATKINS",
    "HUFFMAN",
    "ROY",
    "BOYER",
    "SHIELDS",
    "LIN",
    "HANCOCK",
    "GRIMES",
    "GLENN",
    "CLINE",
    "DELACRUZ",
    "CAMACHO",
    "DILLON",
    "PARRISH",
    "ONEILL",
    "MELTON",
    "BOOTH",
    "KANE",
    "BERG",
    "HARRELL",
    "PITTS",
    "SAVAGE",
    "WIGGINS",
    "BRENNAN",
    "SALAS",
    "MARKS",
    "RUSSO",
    "SAWYER",
    "BAXTER",
    "GOLDEN",
    "HUTCHINSON",
    "LIU",
    "WALTER",
    "MCDOWELL",
    "WILEY",
    "RICH",
    "HUMPHREY",
    "JOHNS",
    "KOCH",
    "SUAREZ",
    "HOBBS",
    "BEARD",
    "GILMORE",
    "IBARRA",
    "KEITH",
    "MACIAS",
    "KHAN",
    "ANDRADE",
    "WARE",
    "STEPHENSON",
    "HENSON",
    "WILKERSON",
    "DYER",
    "MCCLURE",
    "BLACKWELL",
    "MERCADO",
    "TANNER",
    "EATON",
    "CLAY",
    "BARRON",
    "BEASLEY",
    "ONEAL",
    "SMALL",
    "PRESTON",
    "WU",
    "ZAMORA",
    "MACDONALD",
    "VANCE",
    "SNOW",
    "MCCLAIN",
    "STAFFORD",
    "OROZCO",
    "BARRY",
    "ENGLISH",
    "SHANNON",
    "KLINE",
    "JACOBSON",
    "WOODARD",
    "HUANG",
    "KEMP",
    "MOSLEY",
    "PRINCE",
    "MERRITT",
    "HURST",
    "VILLANUEVA",
    "ROACH",
    "NOLAN",
    "LAM",
    "YODER",
    "MCCULLOUGH",
    "LESTER",
    "SANTANA",
    "VALENZUELA",
    "WINTERS",
    "BARRERA",
    "ORR",
    "LEACH",
    "BERGER",
    "MCKEE",
    "STRONG",
    "CONWAY",
    "STEIN",
    "WHITEHEAD",
    "BULLOCK",
    "ESCOBAR",
    "KNOX",
    "MEADOWS",
    "SOLOMON",
    "VELEZ",
    "ODONNELL",
    "KERR",
    "STOUT",
    "BLANKENSHIP",
    "BROWNING",
    "KENT",
    "LOZANO",
    "BARTLETT",
    "PRUITT",
    "BUCK",
    "BARR",
    "GAINES",
    "DURHAM",
    "GENTRY",
    "MCINTYRE",
    "SLOAN",
    "ROCHA",
    "MELENDEZ",
    "HERMAN",
    "SEXTON",
    "MOON",
    "HENDRICKS",
    "RANGEL",
    "STARK",
    "LOWERY",
    "HARDIN",
    "HULL",
    "SELLERS",
    "ELLISON",
    "CALHOUN",
    "GILLESPIE",
    "MORA",
    "KNAPP",
    "MCCALL",
    "MORSE",
    "DORSEY",
    "WEEKS",
    "NIELSEN",
    "LIVINGSTON",
    "LEBLANC",
    "MCLEAN",
    "BRADSHAW",
    "GLASS",
    "MIDDLETON",
    "BUCKLEY",
    "SCHAEFER",
    "FROST",
    "HOWE",
    "HOUSE",
    "MCINTOSH",
    "HO",
    "PENNINGTON",
    "REILLY",
    "HEBERT",
    "MCFARLAND",
    "HICKMAN",
    "NOBLE",
    "SPEARS",
    "CONRAD",
    "ARIAS",
    "GALVAN",
    "VELAZQUEZ",
    "HUYNH",
    "FREDERICK",
    "RANDOLPH",
    "CANTU",
    "FITZPATRICK",
    "MAHONEY",
    "PECK",
    "VILLA",
    "MICHAEL",
    "DONOVAN",
    "MCCONNELL",
    "WALLS",
    "BOYLE",
    "MAYER",
    "ZUNIGA",
    "GILES",
    "PINEDA",
    "PACE",
    "HURLEY",
    "MAYS",
    "MCMILLAN",
    "CROSBY",
    "AYERS",
    "CASE",
    "BENTLEY",
    "SHEPARD",
    "EVERETT",
    "PUGH",
    "DAVID",
    "MCMAHON",
    "DUNLAP",
    "BENDER",
    "HAHN",
    "HARDING",
    "ACEVEDO",
    "RAYMOND",
    "BLACKBURN",
    "DUFFY",
    "LANDRY",
    "DOUGHERTY",
    "BAUTISTA",
    "SHAH",
    "POTTS",
    "ARROYO",
    "VALENTINE",
    "MEZA",
    "GOULD",
    "VAUGHAN",
    "FRY",
    "RUSH",
    "AVERY",
    "HERRING",
    "DODSON",
    "CLEMENTS",
    "SAMPSON",
    "TAPIA",
    "BEAN",
    "LYNN",
    "CRANE",
    "FARLEY",
    "CISNEROS",
    "BENTON",
    "ASHLEY",
    "MCKAY",
    "FINLEY",
    "BEST",
    "BLEVINS",
    "FRIEDMAN",
    "MOSES",
    "SOSA",
    "BLANCHARD",
    "HUBER",
    "FRYE",
    "KRUEGER",
    "BERNARD",
    "ROSARIO",
    "RUBIO",
    "MULLEN",
    "BENJAMIN",
    "HALEY",
    "CHUNG",
    "MOYER",
    "CHOI",
    "HORNE",
    "YU",
    "WOODWARD",
    "ALI",
    "NIXON",
    "HAYDEN",
    "RIVERS",
    "ESTES",
    "MCCARTY",
    "RICHMOND",
    "STUART",
    "MAYNARD",
    "BRANDT",
    "OCONNELL",
    "HANNA",
    "SANFORD",
    "SHEPPARD",
    "CHURCH",
    "BURCH",
    "LEVY",
    "RASMUSSEN",
    "COFFEY",
    "PONCE",
    "FAULKNER",
    "DONALDSON",
    "SCHMITT",
    "NOVAK",
    "COSTA",
    "MONTES",
    "BOOKER",
    "CORDOVA",
    "WALLER",
    "ARELLANO",
    "MADDOX",
    "MATA",
    "BONILLA",
    "STANTON",
    "COMPTON",
    "KAUFMAN",
    "DUDLEY",
    "MCPHERSON",
    "BELTRAN",
    "DICKSON",
    "MCCANN",
    "VILLEGAS",
    "PROCTOR",
    "HESTER",
    "CANTRELL",
    "DAUGHERTY",
    "CHERRY",
    "BRAY",
    "DAVILA",
    "ROWLAND",
    "MADDEN",
    "LEVINE",
    "SPENCE",
    "GOOD",
    "IRWIN",
    "WERNER",
    "KRAUSE",
    "PETTY",
    "WHITNEY",
    "BAIRD",
    "HOOPER",
    "POLLARD",
    "ZAVALA",
    "JARVIS",
    "HOLDEN",
    "HENDRIX",
    "HAAS",
    "MCGRATH",
    "BIRD",
    "LUCERO",
    "TERRELL",
    "RIGGS",
    "JOYCE",
    "ROLLINS",
    "MERCER",
    "GALLOWAY",
    "DUKE",
    "ODOM",
    "ANDERSEN",
    "DOWNS",
    "HATFIELD",
    "BENITEZ",
    "ARCHER",
    "HUERTA",
    "TRAVIS",
    "MCNEIL",
    "HINTON",
    "ZHANG",
    "HAYS",
    "MAYO",
    "FRITZ",
    "BRANCH",
    "MOONEY",
    "EWING",
    "RITTER",
    "ESPARZA",
    "FREY",
    "BRAUN",
    "GAY",
    "RIDDLE",
    "HANEY",
    "KAISER",
    "HOLDER",
    "CHANEY",
    "MCKNIGHT",
    "GAMBLE",
    "VANG",
    "COOLEY",
    "CARNEY",
    "COWAN",
    "FORBES",
    "FERRELL",
    "DAVIES",
    "BARAJAS",
    "SHEA",
    "OSBORN",
    "BRIGHT",
    "CUEVAS",
    "BOLTON",
    "MURILLO",
    "LUTZ",
    "DUARTE",
    "KIDD",
    "KEY",
    "COOKE"
    ]
