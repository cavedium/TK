# EXAMPLE CODES FOR FUNCTIONS

/**EXAMPLE CODE FOR FUNCTION "is_prime"
    int n;
    cout << "Enter the number: ";
    cin >> n;
    is_prime(n);

    if(is_prime(n)){
        cout << n << " is prime" << endl;
    }else{
        cout << n << " is not prime" << endl;
    }
**/

/**EXAMPLE CODE FOR FUNCTION "NSD"
    int x = 36;
    int y = 24;

    cout << NSD(x,y) << endl;
**/

/**EXAMPLE CODE FOR FUNCTION "NSK"
    int x = 6;
    int y = 8;

    cout << NSK(x,y, NSD(x,y)) << endl;
**/

/**EXAMPLE CODE FOR FUNCTION "gorner_system"
    int x, n, p;
    cout << "Enter a number x: ";
    cin >> x;
    cout << "Enter a degree n: ";
    cin >> n;
    cout << "Enter a module p: ";
    cin >> p;

    int result = gorner_system(x, n, p);

    cout << "The result of exaltation " << x << " to a degree " << n << " by module " << p << " = " << result << endl;
**/

/**EXAMPLE CODE FOR FUNCTION "search_generator"
    int n;
    cout << "enter a positive integer: ";
    cin >> n;

    for (int g=2; g<n; g++){
        if(search_generators(g,n)){
            cout << g << " is a generator of " << n << endl;
        }
    }
**/

/**EXAMPLE CODE FOR FUNCTION "legendre_symbol & jacobi_symbol"
    int a, p;
    cout << "Enter number a: ";
    cin >> a;
    cout << "Enter prime number p: ";
    cin >> p;

    int legendre = legendre_symbol(a, p);
    int jacobi = jacobi_symbol(a, p);

    cout << "Legendre symbol for number " << a << " and module " << p << " = " << legendre << endl;
    cout << "Jacobi symbol for a number " << a << " and module " << p << " = " << jacobi << endl;
**/
