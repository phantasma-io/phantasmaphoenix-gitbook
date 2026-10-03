# Carbon Transactions And Fees

A Carbon transaction needs no VM script. The message is built with the helpers
of `PhantasmaPhoenix.Protocol.Carbon`, and one call plans the fee, signs the
message and broadcasts it.

## Sending A Transaction

```csharp
var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var keys = PhantasmaKeys.FromWIF(wif);

var message = NativeTxHelper.TransferFungible(new TransferFungibleParams
{
    From = new Bytes32(keys.PublicKey),
    To = new Bytes32(recipientPublicKey),
    TokenId = 1,
    Amount = 1000
});

StartCoroutine(api.SignAndSendCarbonTransaction(keys, message,
    (txHash, encodedTx) => Debug.Log($"Sent, hash {txHash}"),
    (errorType, errorMessage) => Debug.LogError($"[{errorType}] {errorMessage}")));
```

A Carbon message names the token by its Carbon id, so resolve the symbol first
with `GetToken`. The same result carries the decimals the amount is converted
with.

## The Fee

A message whose `maxGas` is zero is priced against the chain's current gas
configuration before it is signed. The chain refuses an offer of zero. It also
aborts a transaction that spends more gas than it offered, and takes the whole
offer for it.

A message whose `maxGas` you set yourself is signed as it is, and the gas
configuration is not read.

## Showing The Fee Before The Player Confirms

A game has to show what a transaction will cost, and check the balance, before
it asks the player to sign. `PlanCarbonTransaction` prices a message and signs
nothing.

```csharp
FeePlan plan = null;

yield return api.PlanCarbonTransaction(new IKeyPair[] { keys }, message, null,
    result => plan = result,
    (errorType, errorMessage) => Debug.LogError($"[{errorType}] {errorMessage}"));

// plan.MaxGas is the offer the message will carry.
// plan.ExpectedGasBill is what the chain is expected to take out of it.
// Show those, check the balance, and only then sign.

yield return api.SignAndSendCarbonTransaction(keys, plan.Apply(message),
    (txHash, encodedTx) => Debug.Log($"Sent, hash {txHash}"),
    (errorType, errorMessage) => Debug.LogError($"[{errorType}] {errorMessage}"));
```

`FeePlan.Apply` writes the offer into the message. The send path then signs that
message as it is and reads nothing from the chain a second time, so the price
the player approved is the price that is signed.

Pass the same keys the message will be signed with. A `Call`, a `Call_Multi`, a
`Trade` and a `Phantasma` message choose their own witnesses, and the length of
the signed envelope depends on how many there are, so the price depends on the
key count.

The method prices the message and checks nothing else. A successful plan says
the message can be priced. It says nothing about whether the chain will accept
it, and it does not run the token pre-flight.

`plan.Exact` says whether the number is a prediction or a ceiling. Some of the
price depends on chain state the message does not carry, and each such fact is
taken at the reading that costs more. Show the amount when the flag is `true`,
and "up to" in front of the amount when it is `false`.

## Several Signatures

Some transactions need more than one witness. A transfer that names a gas payer
needs the payer and the owner. Use the overload that takes an array of keys,
with one key per witness, in any order:

```csharp
StartCoroutine(api.SignAndSendCarbonTransaction(
    new IKeyPair[] { payerKeys, ownerKeys }, message, null,
    (txHash, encodedTx) => Debug.Log($"Sent, hash {txHash}"),
    (errorType, errorMessage) => Debug.LogError($"[{errorType}] {errorMessage}")));
```

## Creating A Token

A token creation spends the base policy fee before the contract looks at the symbol,
and that fee is the largest single price in the protocol. A creation whose
symbol is already taken spends that fee and creates no token.

So a token creation is checked against the chain first. The symbol is looked up,
and a symbol that resolves to a token is refused before anything is signed. A
symbol that does not resolve comes back as an ordinary error, and an error alone
never means the symbol is free, so a second lookup asks for the gas token by its
id as a control. A node that answers the control is serving token lookups, and
its refusal about your symbol is then a real absence. A node that answers
neither question has established nothing, and the creation is refused for that
reason.

Pass `preflight: false` to skip the check. Nothing else is affected by it.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for every returned asset. The send path reads that from the chain before it
prices the burn.

If you already know what the NFT holds, state it and the chain is not asked:

```csharp
var options = new PlanAndSignOptions { Infusions = infusedAssets };
```

An empty list is a statement too. It says the NFT holds nothing.

## Errors

Everything that goes wrong reaches `errorHandlingCallback`: a refused
pre-flight, a fee that cannot be planned, a key set that does not match the
witnesses the message names, and any network or node failure. Nothing is
broadcast when one of those happens.

## A Worked Example

{% content-ref url="/developers/sdks/unity/examples/send-carbon-token.md" %}
[Send a Carbon Token](/developers/sdks/unity/examples/send-carbon-token.md)
{% endcontent-ref %}
