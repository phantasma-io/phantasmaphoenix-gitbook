# Send a Transaction

This example shows how to send a raw transaction to the Phantasma blockchain. It demonstrates creating a transaction script using the `ScriptBuilder` class, encoding the script, and sending it using the `SendTransaction()` method from the `PhantasmaLinkClient` class.

```csharp
public void SendTransaction()
{
    if (!PhantasmaLinkClient.Instance.IsLogged) return;

    ScriptBuilder sb = new ScriptBuilder();
    var userAddress = Address.Parse(PhantasmaLinkClient.Instance.Address);
    var toAddress = Address.Parse("P2KKEjZK7AbcKZjuZMsWKKgEjNzeGtr2zBiV7qYJHxNXvUa");
    var symbol = "SOUL";
    var amount = UnitConversion.ToBigInteger(1, 8);
    var payload = System.Text.Encoding.UTF8.GetBytes("OurDappExample");
    var script = sb.AllowGas(userAddress, Address.Null, PhantasmaLinkClient.Instance.GasPrice, PhantasmaLinkClient.Instance.GasLimit ).
        CallInterop("Runtime.TransferTokens", userAddress, toAddress, symbol, amount).
        SpendGas(userAddress).
        EndScript();
    
    PhantasmaLinkClient.Instance.SendTransaction("main", script, payload, (hash, s) =>
    {
        if ( hash.IsNull )
        {
            Debug.Log("Transaction failed: " + s);
            return;
        }
        
        Debug.Log("Transaction sent: " + hash);
    });
}
```
