# Connect to the wallet

## Using PhantasmaLink

This is a simple example on how to connect to a wallet.

{% code overflow="wrap" lineNumbers="true" %}
```javascript
let dappID = "Dapp Name";   //This is just the name you want to give the connection
let consoleLogging = true;  //This is if you want console logging for Debugging Purposes [Default is set to true]

let Link = new PhantasmaLink(dappID, consoleLogging); 

Link.login(
    function(success){
        // Handle in case of success.
    }, 
    function(error){
        // Handle in case of error
    }, providerHint);  //Provider Hint can be 'ecto' or 'poltergeist' (It's the name of the wallet the user wants to use to connect.
```
{% endcode %}
