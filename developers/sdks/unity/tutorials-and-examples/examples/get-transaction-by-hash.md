# Get Transaction by Hash

This example demonstrates fetching a transaction's details by its hash. The `GetTransaction()` method from the `PhantasmaAPI` class is used to retrieve the transaction details, which are then passed to the provided callback.

```csharp
public void GetTransaction(string hash, Action<Transaction> callback)
{
    PhantasmaAPI api = new PhantasmaAPI("https://testnet.phantasma.io/rpc");
    StartCoroutine(api.GetTransaction(hash, callback));
}
```
