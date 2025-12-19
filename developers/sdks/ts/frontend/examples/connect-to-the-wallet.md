# Connect to the wallet

## Using PhantasmaLink

This is a simple example on how to connect to a wallet.

{% code overflow="wrap" lineNumbers="true" %}
```ts
import { PhantasmaLink } from "phantasma-sdk-ts";

const dappID = "Dapp Name"; //This is just the name you want to give the connection
const consoleLogging = true; //This is if you want console logging for Debugging Purposes [Default is set to true]

const link = new PhantasmaLink(dappID, consoleLogging);

link.login(
  (success) => {
    // Handle in case of success.
    if (success) {
      console.log("Connected account:", link.account?.address);
    }
  },
  (error) => {
    // Handle in case of error
    console.error("Login failed:", error);
  },
  4, // Phantasma Link protocol version
  "phantasma", // platform
  "poltergeist" //Provider Hint can be 'ecto' or 'poltergeist' (It's the name of the wallet the user wants to use to connect.
);
```
{% endcode %}
