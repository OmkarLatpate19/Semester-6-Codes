function primeChecker(p) {
    // Checks If the number entered is a Prime Number or not
    if (p < 1) {
        return false;
    } else if (p > 1) {
        if (p === 2) {
            return true;
        }
        for (var i = 2; i < p; i++) {
            if (p % i === 0) {
                return false;
            }
        }
        return true;
    }
    return false;
}

function primitiveCheck(g, p) {
    // Checks If The Entered Number Is A Primitive Root Or Not
    var roots = [];
    for (var i = 1; i < p; i++) {
        roots.push(Math.pow(g, i) % p);
    }
    for (var j = 1; j < p; j++) {
        if (roots.filter(function(item) {return item === j}).length > 1) {
            return false;
        }
    }
    return true;
}

function performKeyExchange() {
    var prime = parseInt(document.getElementById('prime').value);
    var root = parseInt(document.getElementById('root').value);
    var aliceSecret = parseInt(document.getElementById('aliceSecret').value);
    var bobSecret = parseInt(document.getElementById('bobSecret').value);

    if (!primeChecker(prime)) {
        alert("Enter a valid prime number (p)");
        return;
    }

    if (!primitiveCheck(root, prime)) {
        alert("Enter a primitive root (g)");
        return;
    }

    // Compute Alice's public value
    var alicePublic = Math.pow(root, aliceSecret) % prime;

    // Compute Bob's public value
    var bobPublic = Math.pow(root, bobSecret) % prime;

    // Compute the shared secret key for Alice
    var aliceSharedKey = Math.pow(bobPublic, aliceSecret) % prime;

    // Compute the shared secret key for Bob
    var bobSharedKey = Math.pow(alicePublic, bobSecret) % prime;

    // Display the shared key
    document.getElementById('sharedKey').innerHTML = "<p>Shared Secret Key for Alice: " + aliceSharedKey + "</p><p>Shared Secret Key for Bob: " + bobSharedKey + "</p>";
}